import sys
import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

from utils import file_path_provided, is_not_empty_txt
from data_handler import get_text_from_file, get_cefr_levels
from text_functionality import create_gap_text


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


def display_mc_lexical_cloze(app_context):
    print("The Exercise 'Multiple Choice Lexical Cloze' will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the exercise.")
    
    pass
    

def display_open_cloze(app_context):
    print("The Exercise 'Open Cloze' will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the exercise.")

    # Convert text to a list of words with gaps ("_")
    cloze_words = create_gap_text(app_context["current_text"])

    # Combine words to text
    cloze = (" ").join(cloze_words)

    # Output the content given
    print(cloze)


def display_word_formation(app_context):
    print("The exercise 'Word Formation' will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the exercise.")
    
    pass
    
    
def display_key_word_transformation(app_context):
    print("The exercise 'Key Word Transformation' will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the exercise.")
    
    pass
    
    
def analyze_speech(app_context):
    print("Here you can let AI analyze your speech.")

    pass


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
    print("==================== Menu ===================")
    print("|1. Display Text                            |")
    print("|2. Exercise: Multiple Choice Lexical Cloze |")
    print("|3. Exercise: Open Cloze                    |")
    print("|4. Exercise: Word Formation                |")
    print("|5. Exercise: Key Word Transformation       |")
    print("|6. Analyze Speech                          |")
    print("|8. View settings                           |")
    print("|9. Exit                                    |")
    print("=============================================")


def main():
    app_context = {
        "is_running": True,
        "current_text": None,
        "current_gap_text": None,
        "current_gap": 0,
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
                call_choice(app_context, choice, display_mc_lexical_cloze)
            case '3':
                call_choice(app_context, choice, display_open_cloze)
            case '4':
                call_choice(app_context, choice, display_word_formation)
            case '5':
                call_choice(app_context, choice, display_key_word_transformation)
            case '6':
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
    
