import os
import pinecone
import langchain.vectorstores import Pinecone
from app.chat.embeddings.opeai import embeddings

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

vector_store = Pinecode.from_existing_index(os.getenv("PINECONE_INDEX_NAME"), embeddings)
