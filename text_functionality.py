from data_handler import get_cefr_levels


def create_gap_text(text):
    """ 
    Create a gap text from a normal text.
    Accepts a text.
    Returns a list of the text with CEFR words replaced by gaps.
    """
    # Prepare the dictionary
    cefr_dict = get_cefr_levels()
    cefr_dict['count'] = [0] * len(cefr_dict['word'])
    
    # Initialize cloze
    cloze = []
    
    for word in text:
        if word in cefr_dict['word']:
            index = cefr_dict['word'].index(word)
            cefr_dict['count'][index] += 1
            word_length = len(word)
            gap = word.replace(word, "_" * word_length) + f" ({cefr_dict['level'][index]})"
            cloze.append(gap)
        else:
            cloze.append(word)
    return cloze
    
            
def get_gap_positions(gap_text):
    """
    Get position of all gaps (underscores).
    Accepts a text as a list of words.
    Returns a list of indexes of the gaps.
    """
    gap_positions = []

    # Gets the indexes of underscores    
    for index, word in enumerate(gap_text):
        if "_" in word:
            gap_positions.append(index)
    
    return gap_positions
    
    
def is_first_or_last_position(gap_text, current_gap_position):
    """
    Get position of current gap (underscore).
    Accepts 
    Returns     
    """
    gap_positions = get_gap_positions(gap_text)
    if current_gap_position == gap_positions[0] or current_gap_position == gap_positions[-1]:
        return True
    return False