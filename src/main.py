# Main Module
from .documents import load_document, chunk_text

document = load_document("data/rag_intro.txt")
print(document)
print(chunk_text("ABCDEFGHIJ", 4))
print(chunk_text("ABC", 10))
print(chunk_text("", 4))
print(chunk_text("ABCDEFGHIJ", 4, 2))
