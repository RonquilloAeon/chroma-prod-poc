from ninja import Router, Schema
from chromadb import Client, Collection
from chromadb.config import Settings

from .serializers import DocumentSerializer

client = Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory=".chromadb"))

router = Router()


@router.post("/documents")
def create_document(request, document: DocumentSerializer):
    # Save the document in Chroma
    embedding_function = None
    collection = Collection(document.account, embedding_function, client=client)
    collection.insert([document.content])

    return {"id": document.id, "title": document.title, "content": document.content}
