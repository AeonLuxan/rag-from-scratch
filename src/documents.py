from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def get_document(topic: str) -> str:
    if not topic.strip():
        raise ValueError("No topic provided")

    return f"Information about {topic}"


def load_document(file_path: str) -> str:
    path = PROJECT_ROOT / file_path
    return path.read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int, overlap: int = 0) -> list[str]:

    if chunk_size <= 0:
        raise ValueError("chunk size must be greater than 0")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and less than chunk size")

    i = 0
    chunks = []
    while i < len(text):
        chunks.append(text[i:i + chunk_size])

        if i + chunk_size >= len(text):
            break

        i += chunk_size - overlap
    return chunks
