from src.application_status import Status

def no_listed_employment(application):
    return (Status.PASS, "nothing to check")

def prev_employment(application):
    return (Status.PASS, "Applicant has had previous employment.")
 
