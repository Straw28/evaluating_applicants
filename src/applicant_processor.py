from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")


def process_applicant(applicant, *criteria):
    if not criteria:
        return no_search_criteria(applicant)

    passed, messages = zip(*(criterion(applicant) for criterion in criteria))
    return (Status.FAIL, " ".join(messages)) if any(status == Status.FAIL for status in passed) else (Status.PASS, " ".join(messages))