from importlib import import_module

def fetch_criterion(sort_function, path='src.criteria'):
    sorting_module = import_module(f'{path}.applicant_{sort_function}')
    return getattr(sorting_module, 'evaluate_application')
