from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")


def process_applicant(applicant, *criteria):

    if not criteria:
        return no_search_criteria(applicant)

    if callable(criteria):
        criteria = [criteria]

    results = tuple(criterion(applicant) if callable(criterion) else applicant for criterion in criteria)

    return results