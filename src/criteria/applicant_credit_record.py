from application_status import Status

def evaluate_application(application): 
    return (Status.PASS, "Applicant has a good credit record.")\
        if application.has_good_credit_record else (Status.FAIL, "Applicant has a bad credit record.")
 