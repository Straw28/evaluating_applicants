from dataclasses import dataclass

@dataclass
class Applicant:
    is_employed: bool=False
    has_criminal_record: bool=False
