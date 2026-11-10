#Retrievel Module
import string

def retrieval(ques: str, chunks: list[str], top_k: int) -> list[tuple[str,int]]:
    ques_clean = ques.translate(str.maketrans("", "", string.punctuation))
    ques_tokens = list(dict.fromkeys(ques_clean.lower().split()))
    chunk_score = {}
    for chunk in chunks:
        chunk_clean = chunk.translate(str.maketrans("", "", string.punctuation))
        chunk_tokens = chunk_clean.lower().split()
        score = 0
        for token in ques_tokens:
            if token in chunk_tokens:
                 score +=1
        chunk_score[chunk] = score

    chunk_score = {k: v for k,v in chunk_score.items()if v > 0}
    sorted_chunk_score = sorted(chunk_score.items(), key = lambda item: item[1], reverse = True)

    return sorted_chunk_score[:top_k]