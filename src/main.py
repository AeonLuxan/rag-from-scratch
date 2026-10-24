# Main Module
from .documents import load_document

document = load_document("data/rag_intro.txt")
print(document)
