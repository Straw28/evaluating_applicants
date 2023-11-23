from src.application_status import Status
from functools import reduce


def process_applicant(applicant, *criteria):
    if not criteria:
        return (Status.PASS, "nothing to check")

    return reduce(combine_results, [evaluator(applicant) for evaluator in criteria ])

def combine_results(results1, results2):
    status1, message1 = results1
    status2, message2 = results2

    return(Status.PASS if status1 == status2 == Status.PASS else Status.FAIL, " ".join([message1, message2])) 