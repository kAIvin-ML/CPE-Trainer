import re
from collections import Counter

import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

from data_handler import get_cefr_levels
from presentation import separator_hyphen_75


def call_choice(app_context, choice, func):
    """
    Calls the desired exercise (function).
    """
    separator_hyphen_75()
    print(f"You selected: {choice}.")
    func(app_context)
    separator_hyphen_75()


def split_text_into_words(text):
    """
    Splits the text into a list of words with the blank delimiter.
    Accepts a text as a string.
    Returns a list of words.
    """
    words = text.split(" ")
    return words


def split_text_into_sentences(text):
    """
    Splits the text into a list of sentences.
    Accepts a text as a string.
    Returns a list of sentences.
    """
    sentences = sent_tokenize(text)
    return sentences


def create_gap_text(text):
    """ 
    Create a gap text from a normal text.
    Accepts a text as a list of words.
    Returns a list of words with CEFR words replaced by gaps.
    """
    # Prepare the dictionary of CEFR words (word, level and count)
    cefr_dict = get_cefr_levels()
    cefr_dict['count'] = [0] * len(cefr_dict['word'])
    
    # Define gap string
    replacement_string = "______"
    
    # Replacement
    ## Define words to search for
    words_to_replace = cefr_dict["word"]
    pattern = r'\b(' + '|'.join(words_to_replace) + r')\b' # Ensures that all selected words will be replaced
    ## Create gap text while ignoring casing
    gap_text = re.sub(pattern, replacement_string, text, flags=re.IGNORECASE)
    ## Find all replaced words and insert them into a list while ignoring casing
    replaced_words = re.findall(pattern, text, re.IGNORECASE)
    replaced_words_lower_case = [word.lower() for word in replaced_words]
    
    # Frequency
    ## Get the frequency of all replaced words
    word_counts = Counter(replaced_words_lower_case)
    ## Update the CEFR dictionary with word counts for statistical purposes
    for word, count in word_counts.items():
        word_index = cefr_dict["word"].index(word)
        cefr_dict["count"][word_index] = count
    
    return gap_text


def get_gap_positions(gap_text):
    """
    Get position of all gaps (underscores).
    Accepts a text as a list of words where selected words have been replaced with gaps.
    Returns a list of indexes of the gaps.
    """
    gap_positions = []

    # Gets the indexes of underscores    
    for index, sentence in enumerate(gap_text):
        if "_" in sentence:
            gap_positions.append(index)
    
    return gap_positions