# from src.applicant import Applicant
# from src.applicant_processor import process_applicant
from fetch_criteria import fetch_criteria
# from src.fetch_criterion import fetch_criterion

def display_menu(path):
    print("Select criterias to evaluate the following applicant: ")
    for menu_num, criterion in enumerate(fetch_criteria(path), start=1):
        print(f"{menu_num}. {criterion}")

def


if __name__ == "__main__":
    display_menu('src/criteria')