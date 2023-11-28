import unittest
import sys
sys.path.append('src')
from criteria.applicant_credit_record import evaluate_application as check_credit_record
from application_status import Status
from applicant import Applicant

class TestCreditRecordCriteria(unittest.TestCase):
   
    def test_credit_records_returns_pass(self):
        application = Applicant(has_good_credit_record=True)
        status, message = check_credit_record(application)

        self.assertEqual((status, message), (Status.PASS, "Applicant has a good credit record."))

    def test_credit_records_returns_fail(self):
        application = Applicant(has_good_credit_record=False)
        status, message = check_credit_record(application)        
        
        self.assertEqual((status, message), (Status.FAIL, "Applicant has a bad credit record."))
