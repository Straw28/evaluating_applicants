from src.application_status import Status

def evaluate_application(application): 
    return (Status.PASS, "Applicant meets security clearance requirements.")\
        if application.has_security_clearance else (Status.FAIL, "Applicant does not meet security clearance requirements.")