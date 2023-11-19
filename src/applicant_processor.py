from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")


def process_applicant(applicant=(), criteria=()):
    # if not applicant:
    #     pass
    if not criteria:
        return no_search_criteria(applicant)
    return criteria(applicant)
