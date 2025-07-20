def get_text_from_file(path_to_file):
    """
    Retrieve a text - any form of string.
    Always return a string.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
