import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Configure local models
Settings.llm = Ollama(model="llama3.1", request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")

# Load ALL documents from a folder
documents = SimpleDirectoryReader(input_dir="docs").load_data()

# Build index
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(response_mode="compact", text_qa_template=None)

# Streamlit UI
st.title("Local RAG Demo")

user_query = st.text_input("Ask a question about the company policy:")

if user_query:
    response = query_engine.query(user_query)
    st.write(response.response)