import unittest
from src.criteria.applicant_credit_record import evaluate_application as check_credit_record
from src.application_status import Status
from src.applicant import Applicant

class TestApplicant(unittest.TestCase):
   
    def test_credit_records_returns_pass(self):
        application = Applicant(has_good_credit_record=True)
        status, message = check_credit_record(application)

        self.assertEqual((status, message), (Status.PASS, "Applicant has a good credit record."))

    def test_credit_records_returns_fail(self):
        application = Applicant(has_good_credit_record=False)
        status, message = check_credit_record(application)        
        
        self.assertEqual((status, message), (Status.FAIL, "Applicant has a bad credit record."))
