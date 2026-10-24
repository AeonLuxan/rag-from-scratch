from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent


def get_document(topic: str) -> str:
    if not topic.strip():
        raise ValueError("No topic provided")

    return f"Information about {topic}"


def load_document(file_path: str) -> str:
    path = PROJECT_ROOT / file_path
    return path.read_text(encoding="utf-8")