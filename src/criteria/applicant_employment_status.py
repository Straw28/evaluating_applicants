from src.application_status import Status
# from src.applicant import Applicant

def evaluate_application(application): 
    return (Status.PASS, "Applicant has had previous employment.")\
        if application.is_employed else (Status.FAIL, "Applicant has no previous employment.")
 