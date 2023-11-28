from application_status import Status

def evaluate_application(application): 
    return (Status.PASS, "Applicant has had previous employment.")\
        if application.is_employed else (Status.FAIL, "Applicant has no previous employment.")
 