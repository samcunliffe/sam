"""Miscellaneous useful functions"""

def lensort(list_of_objects_with_length):
    """Sorts list objects by len"""
    return sort(list_of_objects_with_length, key=len)

def flatten_list_of_tuples(li):
    """flattens a list of tuples, eg. from a 'zip', into a single list"""
    return list(sum(li, ()))


def is_string(st):
    """checks what you just gave me is a string"""
    return str(st) == st

def mkdir(dirname):
    """Performs the equivalent of bash shell mkdir -p"""
    from os import system as run_command
    return run_command('mkdir -p ' + dirname)
