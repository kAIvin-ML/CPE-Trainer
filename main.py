import sys
import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from utils import file_path_provided, is_not_empty_txt
from data_handler import get_text_from_file, get_cefr_levels


def main():

    # Initialize time variable for naming
    now = dt.datetime.now()
    timestamp = now.strftime("%Y_%m_%d__%H_%M_%S")

    # Load a text file
    if file_path_provided(sys.argv) and is_not_empty_txt(sys.argv[1]):
        text_path = sys.argv[1]
    text = get_text_from_file(text_path)
    words = text.split(" ")

    # Generate and save word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    # plt.show() # --> Can be enabled

    # wordcloud.to_file(f"stats/wordcloud_{timestamp}.png") # Can be enabled to save the wordcloud

    # Map words to CEFR levels
    cefr_dict = get_cefr_levels()

    cloze = []

    # Create gap cloze
    for word in words:
        if word in cefr_dict['word']:
            word_length = len(word)
            gap = word.replace(word, "_" * word_length)
            cloze.append(gap)
        else:
            cloze.append(word)

            # Creates stats
            pass
    gap_cloze = (" ").join(cloze)

    # Output the content given
    print("==========BEGIN=========")
    print(gap_cloze)
    print("=========END=========")


if __name__ == "__main__":
    main()
