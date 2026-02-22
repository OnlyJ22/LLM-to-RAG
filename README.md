# LLM to RAG Setup Guide

## Project Description

This project demonstrates how to build a fully local Retrieval-Augmented Generation (RAG) system using Ollama, Llama 3.1, LlamaIndex, and ChromaDB. The setup loads a local document (`company_policy.txt`), converts it into embeddings, stores it in a vector index, and allows the LLM to answer questions using retrieved context from that document. Everything runs locally — no cloud services or API keys required.

## Step 1 – Download Ollama

Go to: https://ollama.com/download

Select your operating system:
- Windows
- macOS
- Linux

Download and install Ollama.

---

## Step 2 – Pull the Llama 3.1 Model

Open a Terminal (Command Prompt, PowerShell, or Terminal).

Run the following command:

```bash
ollama pull llama3.1
```

> **Note:** This command downloads the model locally to your machine.

---

## Step 3 – Run the Model

To start using the model, run:

```bash
ollama run llama3.1
```

You can now interact with the Llama 3.1 model directly from your terminal.

## Step 1 – Python 3.12.10

Download from: https://www.python.org/downloads/release/python-31210/

**Windows installer (64-bit)** — Recommended

> **Important installation steps:**
> 1. Check **"Add python.exe to PATH"** before clicking anything, then click **Install Now**
> 2. Before closing, click **"Disable path length limit"** — this removes a Windows limitation that can cause issues with Python packages

Python 3.12.10 confirmed and working.

---

## Step 2 – Pull the Embedding Model
```bash
ollama pull nomic-embed-text
```

---

## Step 3 – Install Dependencies

Run the following in PowerShell:
```bash
pip install llama-index chromadb llama-index-vector-stores-chroma llama-index-embeddings-ollama llama-index-llms-ollama
```

**What each package does:**

| Package | Purpose |
|---|---|
| `llama-index` | Main RAG orchestration framework — the glue connecting everything |
| `llama-index-llms-ollama` | Connector that lets LlamaIndex talk to your local Ollama/Llama 3.1 model |
| `llama-index-embeddings-ollama` | Connector that lets LlamaIndex use your `nomic-embed-text` embedding model via Ollama |
| `llama-index-vector-stores-chroma` | Connector between LlamaIndex and ChromaDB |
| `chromadb` | Vector database that stores your document embeddings |

## Step 1 – Add `rag.py`

Create a file named:

```
rag.py
```

Paste the following code into `rag.py`:

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Configure local models
Settings.llm = Ollama(model="llama3.1", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Load your document
documents = SimpleDirectoryReader(input_files=["company_policy.txt"]).load_data()

# Build the index
index = VectorStoreIndex.from_documents(documents)

# Create query engine
query_engine = index.as_query_engine()

# Ask a question
response = query_engine.query("What is the refund policy for enterprise customers?")
print(response)
```

---

## Step 1 – Create `company_policy.txt`

In the same folder as `rag.py`, create a file named:

```
company_policy.txt
```

Add the following content:

```txt
Enterprise customers receive a 60 day refund window.
Refund requests must be submitted via the enterprise portal.
Standard customers receive a 30 day refund window.
All refund requests require a valid order number.
Contact support@company.com for refund assistance.
```


## Step 1 — Install Streamlit

Streamlit is a lightweight Python framework that allows you to build interactive web apps quickly.

Install it by running:

```bash
pip install streamlit
```

If `pip` does not work, use:

```bash
python -m pip install streamlit
```

Verify installation:

```bash
streamlit --version
```

If installed correctly, it will display the installed version number.

---

## Step 1 — Create the Application File

Inside your project folder (`LLM-to-RAG`), create a new file:

```
app.py
```

Make sure this file is in the same directory as:

- `rag.py`
- `company_policy.txt`

---

## Step 1 — Add the Streamlit RAG Code

Paste the following into `app.py`:

```python
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Configure local models
Settings.llm = Ollama(model="llama3.1", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Load document
documents = SimpleDirectoryReader(
    input_files=["company_policy.txt"]
).load_data()

# Build index
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Streamlit UI
st.title("Local RAG Demo")

user_query = st.text_input("Ask a question about the company policy:")

if user_query:
    response = query_engine.query(user_query)
    st.write(response.response)
```

Save the file before continuing.

---

## Step 1 — Run the Web App

Start the Streamlit application with:

```bash
streamlit run app.py
```

This will open a local web interface in your browser.