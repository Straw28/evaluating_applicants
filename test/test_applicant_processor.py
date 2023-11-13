import unittest
from src.applicant_processor import process_applicant

class TestApplicant(unittest.TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_no_criteria_returns_pass(self):
        result = ["pass", "empty applicant"]
        application = []

        self.assertEqual(process_applicant(application), ["pass", "no search criteria"])
    