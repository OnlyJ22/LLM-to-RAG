# LLM to RAG Setup Guide

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
