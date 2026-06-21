from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
import io
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# --- Global Variables for Local Model Management ---
MODEL_NAME = "gemma4:e4b" # Assuming this is the model name used locally
tokenizer = None
model = None


# --------------------------------------------------------
# Model Initialization Function (Runs ONLY ONCE when server starts)
def load_local_llm():
    """Loads the Gemma model and tokenizer into memory."""
    print("\n[INFO] Starting LLM loading process. This may take several minutes...")
    try:
        # Load Tokenizer first
        global tokenizer
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

        # Load Model using quantization for efficiency (recommended)
        global model
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME, 
            torch_dtype=torch.bfloat16, # Use bfloat16 if GPU supports it
            device_map="auto"           # Automatically use GPU/CPU
        )
        print("\n[SUCCESS] Gemma Model loaded successfully into memory!")

    except Exception as e:
        print(f"\n!!! FATAL ERROR LOADING MODEL !!!")
        print(f"Ensure you have sufficient VRAM/RAM and the model name is correct.")
        print(f"Error details: {e}")
        # Exit or raise a fatal error if the model cannot be loaded
        exit(1) 

# Initialize the FastAPI application instance
app = FastAPI(
    title="Model Context Protocol Service (Local LLM)",
    description="Reads Excel data and transforms it into narrative context for local Gemma model."
)

# Call the initialization function when the app starts up
@app.on_event("startup")
async def startup_event():
    load_local_llm()


# --- FastAPI Endpoint (The main logic remains efficient) ---

@app.post("/process_context/")
async def process_file(file: UploadFile = File(...)):
    """Endpoint to receive an Excel file, extract key insights, and query the local LLM."""
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an .xlsx Excel file.")

    try:
        excel_file_bytes = await file.read()
        df = pd.read_excel(io.BytesIO(excel_file_bytes))
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        raise HTTPException(status_code=500, detail=f"Could not read the Excel file.")

    # 1. Data Transformation (The context generation)
    context = generate_llm_context(df)

    # 2. Local LLM Call
    final_response = local_gemma_call(context, "What are the main trends and business risks presented in this sales data?")
    
    return {
        "status": "success",
        "message": "Context successfully processed and AI response generated locally.",
        "generated_context": context,
        "llm_response": final_response
    }


# --- Helper Functions ---

def generate_llm_context(df: pd.DataFrame) -> str:
    """Analyzes the DataFrame and summarizes its contents into narrative text."""
    # (This function remains identical to the previous version, as it is pure Python logic)
    context_parts = []
    if 'Sales' in df.columns:
        total_sales = df['Sales'].sum()
        avg_sale = df['Sales'].mean()
        max_sale = df['Sales'].max()
        context_parts.append(f"The total reported sales across all records is ${total_sales:,.2f}.")
        context_parts.append(f"The average sale amount recorded is ${avg_sale:,.2f}, with a maximum single sale reaching ${max_sale:,.2f}.")
    
    rows = len(df)
    columns = list(df.columns)
    context_parts.append(f"The dataset contains {rows} records and information across these categories: {', '.join(columns)}.")

    return "\n\n---\n".join(context_parts)


def local_gemma_call(context: str, prompt: str) -> str:
    """Sends the compiled context and prompt to the locally loaded Gemma model."""
    if model is None or tokenizer is None:
        raise RuntimeError("The LLM Model has not been loaded. Check server startup logs.")

    # Prepare the full payload string for the prompt
    prompt_message = f"User Prompt: {prompt}\n\n--- CONTEXT DATA ---\n{context}"

    print("\n[INFO] Generating response from local Gemma model...")
    
    # Tokenize the input message
    input_text = prompt_message
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device) # Move inputs to GPU/CPU device

    # Generate tokens (The core inference call)
    with torch.no_grad():
        outputs = model.generate(
            **inputs, 
            max_new_tokens=512, 
            do_sample=True,       # Use sampling for creative answers
            temperature=0.7       # Adjust temperature to control creativity
        )

    # Decode the generated tokens back into a string
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # The output will include the prompt itself; we clean it up to show only the model's response.
    model_response = generated_text.replace(prompt_message, "").strip()
    return model_response

