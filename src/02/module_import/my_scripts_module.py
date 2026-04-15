import a_library as lib

from a_library import pi_int

def print_pi_list():
    print(f"My pi is: {lib.pi_list=}")

def print_from_pi_int():
    print(f"My from import is: {pi_int=}")

def print_import_pi_int():
    print(f"My module import is: {lib.pi_int=}")
