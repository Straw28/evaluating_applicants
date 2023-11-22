from dataclasses import dataclass

@dataclass
class Applicant:
    is_employed: bool=True
    has_no_criminal_record: bool=True
    has_good_credit_record: bool=True
    has_security_clearance: bool=True

