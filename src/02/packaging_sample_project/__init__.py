import sys

print(f"Init is called. Current name: '{__name__}' in '{__package__}'")

# make sure we can import other modules from our package when it is run directly
# package is None when the module is executed directly (and not imported)
# a module is frozen when it's packaged in an executable that doesn't rely on external dependencies
if __package__ is None and not hasattr(sys, "frozen"):
    import os.path

    # get path of the current file
    path = os.path.realpath(os.path.abspath(__file__))
    # add current directory to the list of directories the interpreter searches when a module is required
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

# import things form your module here!
from packaging_sample_project import some_functions
# import some_functions as sf

if __name__ == '__main__':
    some_functions.a_first_function()
    # sf.a_first_function()
