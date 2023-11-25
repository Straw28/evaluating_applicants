#keeps calling fetch criterion until done?
from importlib import import_module

#will we pass sort_function as a tuple this time?
def fetch_criterion(sort_function, path='src.criteria'):
    possible_criteria = ['sort_function1', 'sort_function2', 'sort_function3']  # Add your sort functions here

    sorting_module = import_module(f'{path}.applicant_{sort_function}')
    print("sorting mod:", sorting_module)
    return getattr(sorting_module, 'evaluate_application')