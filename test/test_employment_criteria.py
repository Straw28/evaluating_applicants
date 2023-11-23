import unittest
from src.criteria.applicant_employment_status import evaluate_application as check_employment
from src.application_status import Status
from src.applicant import Applicant

class TestApplicant(unittest.TestCase):
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.application_with_no_employment = Applicant(False)

    def test_canary(self):

        self.assertTrue(True)
        
    def test_employment_criteria_returns_pass(self):
        status, message = check_employment(self.application_with_employment)

        self.assertEqual(status, message, Status.PASS) #Feedback: what's the message? Why only status? Would having only status help each of the criteria conform to the expectations that process_applicant has for each criteria?

    def test_employment_criteria_returns_fail(self):
        status, message = check_employment(self.application_with_no_employment)

        self.assertEqual(status, Status.FAIL)
