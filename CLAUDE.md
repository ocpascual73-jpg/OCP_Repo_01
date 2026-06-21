# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a **Python learning/tutorial repository** based on Deitel & Associates' "Python Fundamentals LiveLessons" series. It spans two editions (1/e and 2/e) and includes standalone projects. The codebase demonstrates Python fundamentals, data visualization, OOP, data science, deep learning, and generative AI APIs.

## Project Structure

### Active Lessons (Python Fundamentals LiveLessons 2/e)
- `01`-`10` — Core Python fundamentals: variables, control flow, functions, sequences, lists, dictionaries, string processing, file I/O, exception handling
- `18` — **Generative AI module**: OpenAI Responses API (text generation, summarization, sentiment analysis, NER), speech-to-text, text-to-speech, image generation, image style transfer, closed captions, content moderation, translation
- `08`-`10` contain `README.md` noting examples are under development
- Each lesson typically has `figXX_XX.py` files (figure examples) and `snippets_py/` (code snippets)

### Legacy Lessons (Python LiveLessons 1/e — `PythonLL1e_llessonXX/`)
- `PythonLL1e_llesson08` — String processing snippets
- `PythonLL1e_llesson09` — Exception handling (`dividebyzero.py`)
- `PythonLL1e_llesson10` — OOP fundamentals (account, card, deck, employee hierarchies, complex numbers, CSV data)
- `PythonLL1e_llesson11` — Word cloud generation (mask images)
- `PythonLL1e_llesson12` — Twitter API data mining (sentiment analysis, tweet streaming)
- `PythonLL1e_llesson13` — Language translation with IBM Watson (deprecated/archived)
- `PythonLL1e_llesson14` — pandas data analysis (weather CSV datasets)
- `PythonLL1e_llesson15` — Deep learning (IMDB RNN, MNIST CNN with TensorBoard)
- `PythonLL1e_llesson16` — Big data (Hadoop, Spark, MongoDB, IoT, PubNub)

### What's New (`whats_new/`)
- Demonstrates newer Python features: `ExceptionGroupDemo.py`, `TypedDictTest.py`, updated OOP examples with employee hierarchies
- Jupyter notebooks for lessons 03-10

### FastAPI Project (`FastAPI/`)
- Standalone web service with two implementations:
  - **`main.py`**: AI Summarizer API — `/summarize` endpoint calls local Ollama (Gemma) for text summarization; `/health` endpoint
  - **`mainxxx.py`**: Model Context Protocol Service — upload `.xlsx` files, extracts insights via pandas, queries a locally-loaded Hugging Face model (Gemma) via transformers/torch
- Dependencies: FastAPI, Pydantic, httpx, pandas, torch, transformers

## Running Code

### Python Scripts
```powershell
# Run any lesson script (some take CLI args)
python 01/RollDieDynamic.py 5 10
python 05/FlipCoin.py 1000
python 05/RollDie.py 1000
```

### FastAPI Server
```powershell
# Terminal 1: Start Ollama (if using local models)
ollama serve

# Terminal 2: Run the FastAPI app
cd FastAPI
uvicorn main:app --reload
# Visit http://localhost:8000/docs for Swagger UI
```

### OpenAI API Examples (Lesson 18)
```powershell
# Requires OPENAI_API_KEY environment variable set
python 18/speech_to_text.py
```

## Running Tests
```powershell
# unittest is configured in .vscode/settings.json
python -m unittest discover -s ./01 -p "*_test.py"
```

## Key Conventions

- **Scripts follow Deitel figure naming**: `figXX_XX.py` corresponds to a book figure
- **CLI arguments** for many scripts: pass number of iterations/rolls/flips as `sys.argv[1]`
- **Jupyter notebooks** co-located with lesson content where applicable
- **API keys** are loaded from environment variables (OpenAI) or from local `keys.py` files (legacy Twitter/IBM Watson examples)
- **Data files** (CSV, images, audio) live in `resources/` subdirectories within lessons
- Documentation comment blocks and copyright headers are preserved from original Deitel sources