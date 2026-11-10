# Main Module
from .documents import load_document, chunk_text
from .retrieval import retrieval


##Load document and create chunks
document = load_document("data/rag_intro.txt")
chunks = chunk_text(document, 100, 20)


##Take user question
ques = input("Ask a question - ")
top_k = 3


##Retrieve relevant chunks
retrieval_response = retrieval(ques, chunks, top_k)


##Output Generation
for i, (chunk, score) in enumerate(retrieval_response, start = 1):
    print(f"Chunk: {i} | Score: {score} \nAnswer: {chunk}")
    print()