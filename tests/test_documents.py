#Testing
import unittest
from src.documents import get_document

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
