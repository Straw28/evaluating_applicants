import unittest
from src.applicant_processor import process_applicant
from src.application_status import Status

class TestApplicant(unittest.TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_no_criteria_returns_pass(self):
        result = [Status.PASS, "no search criteria"]
        application = []

        self.assertEqual(process_applicant(application), result)
    