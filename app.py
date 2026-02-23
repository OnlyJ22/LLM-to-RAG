import streamlit as st
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Configure local models
Settings.llm = Ollama(model="llama3.1", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Streamlit UI
st.title("Local RAG")

# File uploader
uploaded_files = st.file_uploader(
    "Upload documents", 
    accept_multiple_files=True,
    type=["txt", "pdf", "docx", "csv", "md"]
)

# Save uploaded files to docs folder
if uploaded_files:
    os.makedirs("docs", exist_ok=True)
    for file in uploaded_files:
        with open(os.path.join("docs", file.name), "wb") as f:
            f.write(file.getbuffer())
    st.success(f"{len(uploaded_files)} document(s) uploaded successfully")

# Load and index docs folder
if os.path.exists("docs") and os.listdir("docs"):
    documents = SimpleDirectoryReader(input_dir="docs").load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(response_mode="compact", text_qa_template=None)

    user_query = st.text_input("Ask a question about your documents:")

    if user_query:
        response = query_engine.query(user_query)
        st.write(response.response)
else:
    st.info("Please upload at least one document to get started")