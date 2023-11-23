import unittest
from src.criteria.applicant_credit_record import evaluate_application as check_credit_record
from src.application_status import Status
from src.applicant import Applicant

class TestApplicant(unittest.TestCase):
   
    def test_canary(self):

        self.assertTrue(True)

    def test_credit_records_returns_pass(self):
        application = Applicant(has_good_credit_record=True)
        status = check_credit_record(application)

        self.assertEqual(status, Status.PASS)

    def test_credit_records_returns_fail(self):
        application = Applicant(has_good_credit_record=False)
        status = check_credit_record(application)        
        
        self.assertEqual(status, Status.FAIL)
        