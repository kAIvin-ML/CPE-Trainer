import os
from data_handler import get_text_from_file

def file_path_provided(num_arguments):
    """ 
    Checks if a file path has been provided.
    Returns True or an Exception.
    """
    if len(num_arguments) != 2:
        raise Exception("Please try again by providing a file path as the second argument.\nExample: 'python3 main.py [path/to/file/.txt]'")
    return True


def is_txt_file(path_to_file):
    """
    Checks if the provided file is a text file.
    Returns True or an Exception.
    """
    ext = os.path.splitext(path_to_file)[1]
    if ext != ".txt":
        raise Exception("Please try again by providing a .txt file.")
    return True


def  is_not_empty_txt(file):
    """
    Checks if the .txt file is empty.
    Returns True or an Exception.
    """
    if is_txt_file(file):
        num_chars = get_text_from_file(file)
        if len(num_chars) == 0:
            raise Exception("The .txt file is empty. Please provide a file with content.")
        else:
            return True
