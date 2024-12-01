
import unittest
from app.services.resume_parser import parse_resume

class TestResumeParser(unittest.TestCase):
    def test_valid_pdf(self):
        # Assume we have a sample PDF file path (mock or fixture)
        self.assertIsNotNone(parse_resume("sample.pdf"))
    
    def test_unsupported_format(self):
        with self.assertRaises(ValueError):
            parse_resume("unsupported.txt")

if __name__ == "__main__":
    unittest.main()
