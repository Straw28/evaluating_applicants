from src.application_status import Status

def evaluate_application(application): 
    return (Status.PASS)\
        if application.has_security_clearance else (Status.FAIL)