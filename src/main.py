# Main Module
from .documents import load_document, chunk_text

document = load_document("data/rag_intro.txt")
chunks = chunk_text(document, 100, 20)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1} ({len(chunk)} characters):")
    print(chunk)
    print()