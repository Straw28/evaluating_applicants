import unittest
import sys
sys.path.append('src')
from application_status import Status
from applicant import Applicant
from fetch_criterion import fetch_criterion
from fetch_criteria import fetch_criteria

class TestCriteriaFetchers(unittest.TestCase):
   
    def setUp(self):
        self.application_with_employment = Applicant(True)
        self.applicantion_with_employment_and_no_criminal_record = Applicant(True, True)
        self.applicantion_with_employment_and_no_criminal_record_good_credit_clearance = Applicant(True, True, True, True)

        self.criteria_path = 'src/criteria'

    def test_fetch_criterion_employment_status_returns_correctly(self):
        criteria = fetch_criterion('employment_status')
        status, message = criteria(self.application_with_employment)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had previous employment."))

    
    def test_fetch_criterion_criminal_record_returns_correctly(self):
        criteria = fetch_criterion('criminal_record')
        status, message = criteria(self.applicantion_with_employment_and_no_criminal_record)

        self.assertEqual((status, message), (Status.PASS, "Applicant has had no criminal records."))

    def test_fetch_criteria_returns_a_list_of_all_available_including_employment(self):
        criteria_list = fetch_criteria(self.criteria_path)

        self.assertIn(('employment_status'), criteria_list)

    def test_fetch_criteria_returns_a_list_of_all_available_including_criminal_records(self):
        criteria_list = fetch_criteria(self.criteria_path)

        self.assertIn(('criminal_record'), criteria_list)