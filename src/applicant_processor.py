from src.application_status import Status
from src.applicant import Applicant

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")

def process_applicant(applicant=Applicant(False), criteria=()):
    if not criteria:
        return no_search_criteria(applicant)
    return criteria(applicant)
