#Testing
import unittest
from src.documents import get_document, load_document, chunk_text

class TestGetDocument(unittest.TestCase):
    def test_returns_information_about_topic(self):
        result = get_document("RAG")
        self.assertEqual(result, "Information about RAG")

    def test_returns_information_about_different_topic(self):
        result = get_document("AML")
        self.assertEqual(result, "Information about AML")

    def test_empty_topic(self):
        with self.assertRaises(ValueError):
            get_document("")

    def test_whitespace_topic(self):
        with self.assertRaises(ValueError):
            get_document("   ")

    def test_load_document(self):
        document = load_document("data/rag_intro.txt")
        self.assertIn("text generation", document)

    def test_missing_document_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            load_document("data/does_not_exist.txt")

    def test_chunk_text(self):
        text = "ABCDEFGH"
        self.assertEqual(chunk_text(text, 2), ["AB", "CD", "EF", "GH"])

    def test_chunk_text_chunk_size_greater_than_text_length(self):
        text = "ABCDEFGH"
        self.assertEqual(chunk_text(text, 10), ["ABCDEFGH"])

    def test_chunk_text_empty_string(self):
        text = ""
        self.assertEqual(chunk_text(text, 4), [])

    def test_chunk_text_chunk_size_zero(self):
        text = "ABCDEFGH"
        with self.assertRaises(ValueError):
            chunk_text(text, 0)

    def test_chunk_text_negative_chunk_size(self):
        with self.assertRaises(ValueError):
            chunk_text("ABCDEFGH", -2)

    def test_chunk_text_with_overlap(self):
        self.assertEqual(
            chunk_text("ABCDEFGHIJ", 4, 2),
            ["ABCD", "CDEF", "EFGH", "GHIJ"],
        )

    def test_chunk_text_overlap_equals_chunk_size(self):
        with self.assertRaises(ValueError):
            chunk_text("ABCDEFGH", 4, 4)

    def test_chunk_text_negative_overlap(self):
        with self.assertRaises(ValueError):
            chunk_text("ABCDEFGH", 4, -1)