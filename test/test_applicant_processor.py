import unittest
from src.applicant_processor import process_applicant
from src.application_status import Status
from src.applicant import Applicant
from src.criteria.applicant_employment_status import employment_status

class TestApplicant(unittest.TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_no_criteria_returns_pass(self):
        result = (Status.PASS, "nothing to check")
        application = Applicant()

        self.assertEqual(process_applicant(application), result)
    
    def test_one_criteria_employment_status_returns_expected_result(self):
        result = (Status.PASS, "Applicant has had previous employment.")
        application = Applicant(True)
        criteria = employment_status

        self.assertEqual(process_applicant(application, criteria), result)
