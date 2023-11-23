import unittest
from src.criteria.applicant_criminal_record import evaluate_application as check_criminal_record
from src.application_status import Status
from src.applicant import Applicant

class TestApplicant(unittest.TestCase):
    
    def test_criminal_record_returns_pass(self):
            application = Applicant(has_no_criminal_record=True)
            status, message = check_criminal_record(application)
        
            self.assertEqual((status, message), (Status.PASS, "Applicant has had no criminal records."))

    def test_criminal_record_returns_fail(self):
            application = Applicant(has_no_criminal_record=False)
            status, message = check_criminal_record(application)
            
            self.assertEqual((status, message), (Status.FAIL, "Applicant has had criminal records."))
