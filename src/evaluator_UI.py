from applicant import Applicant
from applicant_processor import process_applicant
from fetch_criteria import fetch_criteria
from fetch_criterion import fetch_criterion


def display_menu(path):
    print("Application Evaluation Criteria List: ")
    for menu_num, criterion in enumerate(fetch_criteria(path), start=1):
        print(f"{menu_num}. {criterion}")

def get_user_criteria():
    while True:
        try:
            user_input = input("Choose criteria number(s) separated by commas: ")
            chosen_menu_numbers = tuple(map(int, user_input.split(',')))
            
            return chosen_menu_numbers
        except ValueError:
            print("Invalid input. Please enter a valid criteria number from the menu separated by commas.")

def grab_criteria_by_number(user_response):
    criteria_names = fetch_criteria('src/criteria')
    chosen_criteria = [criteria_names[menu_num - 1] for menu_num in user_response if 1 <= menu_num <= len(criteria_names)]
    return tuple(chosen_criteria)

def process_applicant_info(question: str) -> bool:
        while True:
            try:
                user_input = input(f"{question} (True/False): ").lower()
                if user_input in ['true', 'false']:
                    return user_input == 'true'
                raise ValueError
            except ValueError:
                print("Invalid input. Please enter True or False.")

def get_application_info():
    print("Provide applicant details:")
    is_employed = process_applicant_info("Is the applicant employed?")
    has_no_criminal_record = process_applicant_info("Does the applicant have no criminal record?")
    has_good_credit_record = process_applicant_info("Does the applicant have a good credit record?")
    has_security_clearance = process_applicant_info("Does the applicant have security clearance?")

    return Applicant(is_employed, has_no_criminal_record, has_good_credit_record, has_security_clearance)


def add_applicant_valid_response():
        while True:
            try:
                user_input = input("Would you like to process another application? Please enter Yes or No: ").lower()
                if user_input == 'yes':
                    return True
                elif user_input == 'no':
                    return False
                raise ValueError
            except ValueError:
                print("Invalid input. Please enter Yes or No.")
                
if __name__ == "__main__": 
    display_menu('src/criteria')
    chosen_criteria = grab_criteria_by_number(get_user_criteria()) 
    criteria_functions = [fetch_criterion(criterion, 'criteria') for criterion in chosen_criteria]
    
    continue_entering_applicants = True
    
    while continue_entering_applicants:

        new_applicant = get_application_info()
        print(process_applicant(new_applicant, *criteria_functions))

        continue_entering_applicants = add_applicant_valid_response()