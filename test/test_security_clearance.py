import unittest
import sys
sys.path.append('src')
from criteria.applicant_security_clearance import evaluate_application as check_security_clearance
from application_status import Status
from applicant import Applicant

class TestSecurityClearenceCriteria(unittest.TestCase):
   
    def test_security_clearance_returns_pass(self):
        application = Applicant(has_security_clearance=True)
        status, message = check_security_clearance(application)
        
        self.assertEqual((status, message), (Status.PASS, "Applicant meets security clearance requirements."))

    def test_security_clearance_returns_fail(self):
        application = Applicant(has_security_clearance=False)
        status, message = check_security_clearance(application)
        
        self.assertEqual((status, message), (Status.FAIL, "Applicant does not meet security clearance requirements."))
