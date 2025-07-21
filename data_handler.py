import csv


def get_text_from_file(path_to_file):
    """
    Retrieve a text - any form of string.
    Always return a string.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def get_cefr_levels():
    """
    Loads a CSV with the CEFR levels.
    Returns a dictionary of words and levels.
    E.g. {'word': ['will', 'one', 'though'], 'level': ['A1', 'A1', 'A1 A2']}
    """

    # Data source does not change
    path_to_csv = f"data/CEFR_levels_dummy_file.csv"

    # Initialize a dictionary
    word_level_pairs = dict()

    # Read the rows
    with open(path_to_csv, 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file) # Reads the head row
        for row in reader:
            for word, level in row.items():
                word_level_pairs.setdefault(word, []).append(level)
    return word_level_pairs
