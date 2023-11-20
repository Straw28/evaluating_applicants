from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")


def process_applicant(applicant=(), criteria=()):
    results = []

    if not criteria:
        return no_search_criteria(applicant)

    if callable(criteria):
        criteria = [criteria]

    result = applicant

    for criterion in criteria:
        result = criterion(result) if callable(criterion) else result
        results.append(result)

    return results