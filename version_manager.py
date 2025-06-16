from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Embedding function
embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Create new ChromaDB client (✨ updated way)
client = PersistentClient(path="chroma_store")

# Try to get existing collection, else create it with embedding function
try:
    collection = client.get_collection("book_versions_v2")
except Exception:
    collection = client.get_or_create_collection("book_versions_v2", embedding_function=embedding_fn)


def save_version(title, content):
    doc_id = title.replace(" ", "_").lower()
    collection.add(
        documents=[content],
        ids=[doc_id],
        metadatas=[{"title": title}]
    )
    print(f"📚 Saved final version under ID: {doc_id}")
