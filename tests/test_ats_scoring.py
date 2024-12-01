
import unittest
from app.services.ats_scoring import calculate_ats_score

class TestATSScoring(unittest.TestCase):
    def test_keyword_match(self):
        resume_text = "Python Java Teamwork Communication"
        job_description = "Python, Java, Leadership"
        score = calculate_ats_score(resume_text, job_description)
        self.assertGreater(score["keyword_score"], 0)

if __name__ == "__main__":
    unittest.main()
