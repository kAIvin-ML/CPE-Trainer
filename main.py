import sys
import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

from utils import file_path_provided, is_not_empty_txt
from data_handler import get_text_from_file, get_cefr_levels


def call_choice(choice, func):
    separator_str = "-" * 75
    print(separator_str)
    print(f"You selected: {choice}.")
    continue_running = func()
    print(separator_str)

    return continue_running


def display_text():
    print("The text will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the text.")
    
    # Code to display the text
    
    return True


def display_gap_cloze():
    print("The gap cloze will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the text.")

    # Code to display the gap cloze
    
    return True    


def generate_exercises():
    print("Here you can generate some exercises with Gen AI.")

    # Code to generate some exercises
    
    return True  


def analyze_speech():
    print("Here you can let AI analyze your speech.")

    # Code to analyze your speech
    
    return True  


def view_settings():
    print("Your settings are:")

    # Code to show the settings
    
    return True    
    
    
def exit_app():
    print("Exiting application.")

    return False


def display_menu():
    print("========== Menu ==========")
    print("|1. Display text         |")
    print("|2. Display gap cloze    |")
    print("|3. Generate exercise    |")
    print("|4. Analyze speech       |")
    print("|8. View settings        |")
    print("|9. Exit                 |")
    print("==========================")


def main():
    app_context = {
        "is_running": True,
        "current_text": None,
        "text_file_path": None
    }
    
    while app_context["is_running"]:
        display_menu()
        choice = input("Please enter your choice by entering the corresponding number: ")
        match choice:
            case '1':
                continue_running = call_choice(choice, display_text)
            case '2':
                continue_running = call_choice(choice, display_gap_cloze)
            case '3':
                continue_running = call_choice(choice, generate_exercises)
            case '4':
                continue_running = call_choice(choice, analyze_speech)
            case '8':
                continue_running = call_choice(choice, view_settings)
            case '9':
                continue_running = call_choice(choice, exit_app)
            case _:
                print("Invalid choice. Please enter a number from the menu.")
                input("\nPress Enter to continue...")
                continue

        app_context["is_running"] = continue_running
                
        if app_context["is_running"]:
            input(">>> Press Enter to display the menu again. <<<")


"""

    # Initialize time variable for naming
    now = dt.datetime.now()
    timestamp = now.strftime("%Y_%m_%d__%H_%M_%S")

    text_path = sys.argv[1]
    text = get_text_from_file(text_path)

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


"""


if __name__ == "__main__":
    main()
