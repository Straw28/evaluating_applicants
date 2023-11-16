from src.criteria.applicant_employment_status import no_listed_employment

def process_applicant(applicant, criteria=no_listed_employment):
    return criteria(applicant)
