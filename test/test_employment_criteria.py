import unittest
import sys
sys.path.append('src')
from criteria.applicant_employment_status import evaluate_application as check_employment
from application_status import Status
from applicant import Applicant

class TestEmploymentStatusCriteria(unittest.TestCase):
    
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.application_with_no_employment = Applicant(False)
 
    def test_employment_criteria_returns_pass(self):
        status, message = check_employment(self.application_with_employment)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had previous employment."))

    def test_employment_criteria_returns_fail(self):
        status, message = check_employment(self.application_with_no_employment)

        self.assertEqual((status, message), (Status.FAIL, "Applicant has no previous employment."))
