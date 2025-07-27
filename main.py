import sys
import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

from utils import file_path_provided, is_not_empty_txt
from data_handler import get_text_from_file, get_cefr_levels


def call_choice(app_context, choice, func):
    separator_str = "-" * 75
    print(separator_str)
    print(f"You selected: {choice}.")
    func(app_context)
    print(separator_str)
    

def display_text(app_context):
    # Initialize time variable for naming
    now = dt.datetime.now()
    timestamp = now.strftime("%Y_%m_%d__%H_%M_%S")
    
    print("The text will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the text.")
    
    # Code to display the text
    text = " ".join(app_context["current_text"])
    print(text)
    
    # Generate and save word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    # plt.show() # --> Can be enabled

    # Save wordcloud
    wordcloud.to_file(f"stats/wordcloud_{timestamp}.png")
    
    # Create stats of word difficulty and frequency
    cefr_dict = get_cefr_levels()
    word_frequency_dict = {
        "word": [],
        "frequency": []
    }
    for word in cefr_dict["word"]:
        word_frequency = text.count(word)
        if word_frequency > 0:
            word_frequency_dict["word"].append(word)
            word_frequency_dict["frequency"].append(word_frequency)
    df_word_frequency = pd.DataFrame(word_frequency_dict)
    sorted_df_w_freq = df_word_frequency.sort_values(by="frequency", ascending = False)
    sorted_df_file_name = f"stats/text_analyzed_{timestamp}.csv"
    sorted_df_w_freq.to_csv(sorted_df_file_name, index = False)
    print("Saved statistics to folder 'stats'.")


def display_gap_cloze(app_context):
    print("The gap cloze will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the text.")

    # Code to display the gap cloze

    # Prepare the dictionary
    cefr_dict = get_cefr_levels()
    cefr_dict['count'] = [0] * len(cefr_dict['word'])

    cloze = []

    # Create gap cloze
    for word in app_context["current_text"]:
        if word in cefr_dict['word']:
            index = cefr_dict['word'].index(word)
            cefr_dict['count'][index] += 1
            word_length = len(word)
            gap = word.replace(word, "_" * word_length) + f" ({cefr_dict['level'][index]})"
            cloze.append(gap)
        else:
            cloze.append(word)

    # Stitch text together
    gap_cloze = (" ").join(cloze)

    # Output the content given
    print("==========BEGIN=========")
    print(gap_cloze)
    print("=========END=========")
    

def generate_exercises(app_context):
    print("Here you can generate some exercises with Gen AI.")

    # Code to generate some exercises


def analyze_speech(app_context):
    print("Here you can let AI analyze your speech.")

    # Code to analyze your speech


def view_settings(app_context):
    # Display current text path
    while app_context["text_file_path"] is None:
        print("You haven't selected a text file, yet.")
        app_context["text_file_path"] = input("Please enter your text file path.\nFor instance: 'data/project-gutenberg/pride_and_prejudice.txt'\n")
    
    separator = "=" * 50
    print(separator)
    print(f"Your current text file is:\n{app_context['text_file_path']}")
    print(separator)
    
    # Change the input if desired
    change_source = input("If you want to change the source, please press 1. Otherwise press any key.\n")
    if change_source == '1':
        app_context["text_file_path"] = input("Please enter your new text file path.\n")
        
    # Generate a preview of the first 5 lines
    print(separator)
    print("Preview of the selected text:")
    pass
    print(separator)

    
def exit_app(app_context):
    print("Exiting application.")
    app_context["is_running"] = False


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
        "text_file_path": "texts/project-gutenberg/pride_and_prejudice.txt" #None
    }
    
    text = get_text_from_file(app_context["text_file_path"])
    app_context["current_text"] = text.split(" ")
        
    while app_context["is_running"]:
        display_menu()
        choice = input("Please enter your choice by entering the corresponding number: ")
        match choice:
            case '1':
                call_choice(app_context, choice, display_text)
            case '2':
                call_choice(app_context, choice, display_gap_cloze)
            case '3':
                call_choice(app_context, choice, generate_exercises)
            case '4':
                call_choice(app_context, choice, analyze_speech)
            case '8':
                call_choice(app_context, choice, view_settings)
            case '9':
                call_choice(app_context, choice, exit_app)
            case _:
                print("Invalid choice. Please enter a number from the menu.")
                input("\nPress Enter to continue...")
                continue

        if app_context["is_running"]:
            input(">>> Press Enter to display the menu again. <<<")


if __name__ == "__main__":
    main()
    
