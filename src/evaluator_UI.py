from applicant import Applicant
from applicant_processor import process_applicant
from fetch_criteria import fetch_criteria
# from src.fetch_criterion import fetch_criterion

def display_menu(path):
    print("Select criterias to evaluate the following applicant: ")
    for menu_num, criterion in enumerate(fetch_criteria(path), start=1):
        print(f"{menu_num}. {criterion}")

def get_response():
    while True:
        user_input = input("Enter your menu selections (comma-separated, type 'exit' to finish): ")

        if user_input == 0:
            return []
        
        selections = user_input.split(',')
        try:
            response = [int(selection) for selection in selections]
            return response
        
        except ValueError:
            print("Invalid input. Please enter a comma-separated list of numbers.")

def exit_application(choice):
    return True if choice else False #pass sm else for choice criteria

def create_applicant():
    my_applicant = Applicant()
    return my_applicant

def set_applicant_attributes(applicant, criteria, value):
    for criterion in criteria:
        set_applicant_attributes(new_applicant, criterion, input(f"enter the value of {criterion} (True or False): "))
    applicant.attribute = value #this isn't gonna work.

def get_application_details():
    new_applicant = create_applicant('src/criteria')

    while True:
        display_menu()
        criteria = get_response()
        if exit_application(criteria):
            break

        print(process_applicant(new_applicant, criteria))


if __name__ == "__main__":
    get_application_details()

