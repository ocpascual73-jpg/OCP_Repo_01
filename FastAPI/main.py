### main.py ###
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import httpx

app = FastAPI(title="AI Summarizer API")

# 1. Define Input Validation Schema
class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=50, description="The long text to summarize")
    model: str = Field(default="gemma4", description="Ollama model name")
    max_tokens: int = Field(default=150, ge=10, le=500)

# 2. API Endpoint for Summarization
@app.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    # Ollama's local API URL (default)
    OLLAMA_URL = "http://localhost:11434/api/generate"
    
    # Task-specific prompt engineering
    prompt = f"Summarize the following text concisely in about {request.max_tokens} words:\n\n{request.text}"
    
    payload = {
        "model": request.model,
        "prompt": prompt,
        "stream": False  # Set to True for token-by-token streaming
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            response = await client.post(OLLAMA_URL, json=payload)
            response.raise_for_status()
            
            result = response.json()
            return {
                "summary": result.get("response"),
                "model_used": request.model,
                "status": "success"
            }
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=500, detail=f"Ollama Error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Server Error: {str(e)}")

# 3. Health Check for Monitoring
@app.get("/health")
async def health_check():
    return {"status": "API is active", "ollama_endpoint": "http://localhost:11434"}
