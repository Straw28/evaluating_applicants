from src.application_status import Status

def evaluate_application(application): 
    return (Status.PASS)\
        if application.has_good_credit_record else (Status.FAIL)
 