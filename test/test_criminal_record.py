import unittest
import sys
sys.path.append('src')
from criteria.applicant_criminal_record import evaluate_application as check_criminal_record
from application_status import Status
from applicant import Applicant

class TestCriminalRecordCriteria(unittest.TestCase):
    
    def test_criminal_record_returns_pass(self):
            application = Applicant(has_no_criminal_record=True)
            status, message = check_criminal_record(application)
        
            self.assertEqual((status, message), (Status.PASS, "Applicant has had no criminal records."))

    def test_criminal_record_returns_fail(self):
            application = Applicant(has_no_criminal_record=False)
            status, message = check_criminal_record(application)
            
            self.assertEqual((status, message), (Status.FAIL, "Applicant has had criminal records."))
