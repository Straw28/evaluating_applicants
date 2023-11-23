import unittest
from src.criteria.applicant_security_clearance import evaluate_application as check_security_clearance
from src.application_status import Status
from src.applicant import Applicant

class TestApplicant(unittest.TestCase):
   
    def test_canary(self):

        self.assertTrue(True)
         
    def test_security_clearance_returns_pass(self):
        application = Applicant(has_security_clearance=True)
        status = check_security_clearance(application)
        
        self.assertEqual(status, Status.PASS)

    def test_security_clearance_returns_fail(self):
        application = Applicant(has_security_clearance=False)
        status = check_security_clearance(application)
        
        self.assertEqual(status, Status.FAIL)
