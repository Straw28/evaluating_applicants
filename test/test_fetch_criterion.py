import unittest
import unittest
from src.applicant_processor import process_applicant
from src.application_status import Status
from src.applicant import Applicant
from src.fetch_criterion import fetch_criterion

class TestApplicantProcessor(unittest.TestCase):
   
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.applicantion_with_employment_and_no_criminal_record = Applicant(True, True)
        self.applicantion_with_employment_and_no_criminal_record_good_credit_clearance = Applicant(True, True, True, True)

    def test_fetch_criteria_employment_status_returns_correctly(self):
        criteria = fetch_criterion('employment_status')
        status, message = criteria(self.application_with_employment)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had previous employment."))

    
    def test_fetch_criteria_criminal_record_returns_correctly(self):
        criteria = fetch_criterion('criminal_record')
        status, message = criteria(self.applicantion_with_employment_and_no_criminal_record)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had no criminal records."))

    def test_fetch_criteria_returns_a_list_of_all_available_including_employment(self):
        criteria = fetch_criterion('criminal_record')
        status, message = criteria(self.applicantion_with_employment_and_no_criminal_record_good_credit_clearance)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had no criminal records. Applicant has had previous employment. Applicant has had no criminal records. Applicant has a good credit record. Applicant meets security clearance requirements."))