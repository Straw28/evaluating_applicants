from src.application_status import Status

def employment_status(application):
    return (Status.PASS, "Applicant has had previous employment.") if application.employment_status else (Status.FAIL, "Applicant has not had previous employment.")
 
