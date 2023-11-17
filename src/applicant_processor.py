from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")

def process_applicant(applicant, criteria=no_search_criteria):
    return criteria(applicant)
