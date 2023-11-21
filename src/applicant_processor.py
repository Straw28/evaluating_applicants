from src.application_status import Status

def no_search_criteria(application): 
    return (Status.PASS, "nothing to check")

def collect_passed_criteria_messages(applicant, *criteria):
    return [message for status, message in [criterion(applicant) for criterion in criteria] if status == Status.PASS]

def collect_failed_criteria_messages(applicant, *criteria):
    return [message for status, message in [criterion(applicant) for criterion in criteria] if status == Status.FAIL]

def process_applicant(applicant, *criteria):
    if not criteria:
        return no_search_criteria(applicant)

    return (Status.FAIL, " ".join(collect_failed_criteria_messages(applicant, *criteria))) if len(collect_passed_criteria_messages(applicant, *criteria)) != len(criteria) else (Status.PASS, " ".join(collect_passed_criteria_messages(applicant, *criteria)))
