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

    chunks = []
    i = 0

    while i < len(text):
        # 1. Establish the maximum endpoint
        end = min(i + chunk_size, len(text))

        # 2. Prefer ending at a word boundary
        if end < len(text):
            boundary = text.rfind(" ", i, end)
            if boundary > i:
                end = boundary

        # 3. Store the current chunk
        chunks.append(text[i:end])

        # Stop if we have reached the end
        if end >= len(text):
            break

        # 4. Calculate the intended overlap
        next_i = end - overlap

        # 5. Adjust the next start to a word boundary
        if overlap > 0:
            boundary = text.rfind(" ", i, next_i)
            if boundary > i:
                next_i = boundary + 1

        # Guarantee progress
        if next_i <= i:
            next_i = end

        i = next_i

    return chunks
