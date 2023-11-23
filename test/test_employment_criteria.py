import unittest
from src.criteria.applicant_employment_status import evaluate_application as check_employment
from src.application_status import Status
from src.applicant import Applicant

class TestApplicant(unittest.TestCase):
    
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.application_with_no_employment = Applicant(False)
 
    def test_employment_criteria_returns_pass(self):
        status, message = check_employment(self.application_with_employment)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had previous employment."))

    def test_employment_criteria_returns_fail(self):
        status, message = check_employment(self.application_with_no_employment)

        self.assertEqual((status, message), (Status.FAIL, "Applicant has no previous employment."))
