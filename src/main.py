# Main Module
from .documents import get_document

topic = "retrieval-augmented generation"
document = get_document(topic)
print(document)
