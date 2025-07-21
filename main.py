import sys
import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

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

    # Prepare the dictionary
    cefr_dict = get_cefr_levels()
    cefr_dict['count'] = [0] * len(cefr_dict['word'])

    cloze = []

    # Create gap cloze
    for word in words:
        if word in cefr_dict['word']:
            index = cefr_dict['word'].index(word)
            cefr_dict['count'][index] += 1
            word_length = len(word)
            gap = word.replace(word, "_" * word_length)
            cloze.append(gap)
        else:
            cloze.append(word)

    # Stitch text together
    gap_cloze = (" ").join(cloze)

    # Output the content given
    print("==========BEGIN=========")
    print(gap_cloze)
    print("=========END=========")

    # Creates stats
    df_from_dict = pd.DataFrame(cefr_dict)
    df_sorted = df_from_dict.sort_values(by='count', ascending = False)
    df_file_name = f"stats/text_analyzed_{timestamp}.csv"
    df_sorted.to_csv(df_file_name, index = False)
    print("Saved statistics to folder 'stats'.")


if __name__ == "__main__":
    main()
