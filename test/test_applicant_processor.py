import unittest
from src.applicant_processor import process_applicant
from src.application_status import Status
from src.applicant import Applicant
from src.criteria.applicant_employment_status import prev_employment

class TestApplicant(unittest.TestCase):
    def setUp(self):
        self.application_prev_employment = Applicant(True)

        self.pass_no_check = (Status.PASS, "nothing to check")
        self.pass_employed = (Status.PASS, "Applicant has had previous employment.")


    def test_canary(self):
        self.assertTrue(True)

    def test_no_criteria_returns_pass(self):
        result = self.pass_no_check
        application = Applicant()

        self.assertEqual(process_applicant(application), result)
    
    def test_one_criteria_employment_status_returns_expected_result(self):
        result = self.pass_employed
        criteria = prev_employment

        self.assertEqual(process_applicant(self.pass_employed, criteria), result)

