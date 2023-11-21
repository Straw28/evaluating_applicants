from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")


def process_applicant(applicant, *criteria):
    if not criteria:
        return no_search_criteria(applicant)

    processed_results = [criterion(applicant) if callable(criterion) else criterion for criterion in criteria]

    return processed_results[0] if len(processed_results) == 1 else tuple(processed_results)
