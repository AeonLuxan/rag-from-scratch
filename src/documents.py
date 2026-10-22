#Document Retrival
def get_document(topic: str) -> str:
    if not topic.strip():
        raise ValueError("No topic provided")
    
    return f"Information about {topic}"
