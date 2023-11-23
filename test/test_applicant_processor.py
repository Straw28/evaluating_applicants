import unittest
from src.applicant_processor import process_applicant
from src.application_status import Status
from src.applicant import Applicant
from src.criteria.applicant_employment_status import evaluate_application as check_employment
from src.criteria.applicant_criminal_record import evaluate_application as check_criminal_record
from src.criteria.applicant_credit_record import evaluate_application as check_credit_record
from src.criteria.applicant_security_clearance import evaluate_application as check_security_clearance

class TestApplicant(unittest.TestCase):
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.application_with_no_employment = Applicant(False)
        self.applicantion_with_employment_and_no_criminal_record = Applicant(True, True)
        self.applicantion_with_no_employment_and_no_criminal_record = Applicant(False, True)
        self.applicantion_with_employment_and_has_criminal_record = Applicant(True, False)

        self.pass_no_check = (Status.PASS, "nothing to check")
        self.pass_employed = (Status.PASS, "Applicant has had previous employment.")
        self.fail_employed = (Status.FAIL, "Applicant has no previous employment.")
        self.pass_employed_and_no_criminal_record = (Status.PASS, "Applicant has had previous employment. Applicant has had no criminal records.")
        self.fail_employed_and_no_criminal_record = (Status.FAIL, "Applicant has no previous employment. Applicant has had no criminal records.")
        self.fail_employed_and_has_criminal_record = (Status.FAIL, "Applicant has had previous employment. Applicant has had criminal records.")

    def test_canary(self):

        self.assertTrue(True)

    def test_no_criteria_returns_pass(self):
 
        self.assertEqual(process_applicant(self.application_with_employment), self.pass_no_check)
    
    def test_one_criteria_employment_status_returns_expected_pass(self):
  
        self.assertEqual(process_applicant(self.application_with_employment, check_employment), self.pass_employed)

    def test_one_criteria_employment_status_returns_expected_fail(self):

        self.assertEqual(process_applicant(self.application_with_no_employment, check_employment), self.fail_employed)

    def test_two_criteria_employment_and_criminal_status_returns_expected_pass(self):

        self.assertEqual(process_applicant(self.applicantion_with_employment_and_no_criminal_record, check_employment, check_criminal_record), self.pass_employed_and_no_criminal_record)

    def test_two_criteria_employment_fails_criminal_pass_returns_fail(self):

        self.assertEqual(process_applicant(self.applicantion_with_no_employment_and_no_criminal_record, check_employment, check_criminal_record), self.fail_employed_and_no_criminal_record)

    def test_two_criteria_employment_pass_criminal_fails_returns_fail(self):

        self.assertEqual(process_applicant(self.applicantion_with_employment_and_has_criminal_record, check_employment, check_criminal_record), self.fail_employed_and_has_criminal_record)
