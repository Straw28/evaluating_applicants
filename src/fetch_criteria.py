import os 

def fetch_criteria(path):
    file_list = [f.split('applicant_', 1)[-1].split('.')[0] for f in os.listdir(path) if f.startswith('applicant_') and f.endswith('.py')]    
    return tuple(file_list)
