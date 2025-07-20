import sys
import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt

from utils import file_path_provided, is_not_empty_txt
from data_handler import get_text_from_file


def main():

    # Initialize time variable for naming
    now = dt.datetime.now()
    timestamp = now.strftime("%Y_%m_%d__%H_%M_%S")

    # Load a text file
    if file_path_provided(sys.argv) and is_not_empty_txt(sys.argv[1]):
        text_path = sys.argv[1]
    text = get_text_from_file(text_path)

    # Output the content given
    print("==========BEGIN=========")
    print(text)
    print("=========END=========")

    # Generate and save word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off') 
    plt.tight_layout()
    # plt.show() # --> Can be enabled 

    wordcloud.to_file(f"stats/wordcloud_{timestamp}.png")


if __name__ == "__main__":
    main()
