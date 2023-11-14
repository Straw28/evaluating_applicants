from src.application_status import Status
from src.applicant import Applicant

def process_applicant(applicant, criteria=lambda applicant:(Status.PASS, "nothing to check")):
    return criteria(applicant)
