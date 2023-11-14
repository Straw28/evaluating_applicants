from src.application_status import Status

def process_applicant(applicant, criteria=lambda applicant:(Status.PASS, "nothing to check")):
    return criteria(applicant)