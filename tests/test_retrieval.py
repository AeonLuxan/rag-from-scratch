#Testing retrieval

import unittest
from src.retrieval import retrieval


class TestRetrival(unittest.TestCase):
    def test_correct_ranking(self):
        ques = "diabetes insulin"
        chunks = ["Diabetes affects blood glucose", "Insulin regulates blood glucose", "Diabetes and insulin are related"]
        top_k = 3
        retrieved_chunk = retrieval(ques, chunks, top_k)
        self.assertEqual(retrieved_chunk,[('Diabetes and insulin are related', 2), ('Diabetes affects blood glucose', 1), ('Insulin regulates blood glucose', 1)])
    
    def test_case_insensitive_retrieval(self):
        ques = "DIABETES"
        chunks = ["diabetes is a metabolic disease", "HEART DISEASE affects circulation"]
        top_k = 2
        retrieved_chunk = retrieval(ques, chunks, top_k)
        self.assertEqual(retrieved_chunk,[('diabetes is a metabolic disease', 1)])

    def test_no_matching_results(self):
        ques = "oncology"
        chunks = ["Diabetes affects blood glucose", "Insulin regulates blood glucose"]
        top_k = 2
        retrieved_chunk = retrieval(ques, chunks, top_k)
        self.assertEqual(retrieved_chunk,[])
