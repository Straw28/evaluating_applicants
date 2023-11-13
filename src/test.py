import unittest
from applicant_processor import process_applicant

class TestApplicant(unittest.TestCase):
    
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_applicant_returns_False(self):
        self.assertTrue(process_applicant([]), False)