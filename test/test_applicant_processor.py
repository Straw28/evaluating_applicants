import unittest
from src.applicant_processor import process_applicant
from src.application_status import Status
from src.applicant import Applicant
from src.criteria.applicant_employment_status import evaluate_application as check_employment

class TestApplicant(unittest.TestCase):
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.application_with_no_employment = Applicant(False)

        self.pass_no_check = (Status.PASS, "nothing to check")
        self.pass_employed = (Status.PASS, "Applicant has had previous employment.")
        self.fail_employed = (Status.FAIL, "Applicant has no previous employment.")


    def test_canary(self):
        self.assertTrue(True)

    def test_no_criteria_returns_pass(self):
 
        self.assertEqual(process_applicant(self.application_with_employment), self.pass_no_check)
    
    def test_one_criteria_employment_status_returns_expected_pass(self):
  
        self.assertEqual(process_applicant(self.application_with_employment, check_employment), self.pass_employed)

    def test_one_criteria_employment_status_returns_expected_fail(self):
  
        self.assertEqual(process_applicant(self.application_with_no_employment, check_employment), self.fail_employed)
