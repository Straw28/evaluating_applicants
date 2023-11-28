from application_status import Status

def evaluate_application(application): 
    return (Status.PASS, "Applicant has had no criminal records.")\
        if application.has_no_criminal_record else (Status.FAIL, "Applicant has had criminal records.")
