import datetime as dt

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

from data_handler import get_cefr_levels
from text_functionality import create_gap_text, get_gap_positions, split_text_into_sentences
from presentation import clear_screen, separator_equalsign_50


def display_text(app_context):
    # Initialize time variable for naming
    now = dt.datetime.now()
    timestamp = now.strftime("%Y_%m_%d__%H_%M_%S")
    
    print("The text will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the text.")
    
    # Display the text as is
    text = app_context["current_text"]
    print(text)
    
    # Generate wordcloud
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
    print("\nSaved statistics to folder 'stats'.")


def display_mc_lexical_cloze(app_context):
    print("The Exercise 'Multiple Choice Lexical Cloze' will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the exercise.")
    
    pass


def display_open_cloze(app_context):
    print("The Exercise 'Open Cloze' will now be shown.")
    print("To change the text go to settings.")
    input("Press Enter to display the exercise.\n")

    # Behaviour for initial run -> see while loop
    first_run = True
    
    # Convert a text into a gap text
    text = app_context["current_text"]
    
    gap_text = create_gap_text(text)
    splitted_gap_text = split_text_into_sentences(gap_text)
    
    # Get information about gaps for navigation in the while loop
    gap_positions = get_gap_positions(splitted_gap_text)
    current_gap_position = gap_positions[0]
    current_gap_position_idx = gap_positions.index(current_gap_position)
    
    # Main menu of the open cloze
    while True:
        # ------------------------- [0] Preparation -------------------------
        ## Initial display of the gap text on a clean slate
        if first_run == True:
            clear_screen()
            print(f"{splitted_gap_text[current_gap_position]}")
        
        # ------------------------- [1] Question -------------------------
        ## Provides information about hotkeys and asks for user input
        next_action = input(\
            "\n\
            -: previous gap\n\
            +: next gap\n\
            h: get a hint from Gemini\n\
            q: quit exercise\n\n\
            Your input: ").lower()
        
        # ------------------------- [2] Answer -------------------------
        ## Executes on the desired next action
        match next_action:
            ### Go to previous gap
            case '-':
                clear_screen()
                first_run = False
                if current_gap_position_idx - 1 < 0:
                    current_gap_position_idx += 1
                    print("You already reached the beginning of the text.")
        
                current_gap_position_idx -= 1
                current_gap_position = gap_positions[current_gap_position_idx]
                
                print(f"\n\n{splitted_gap_text[current_gap_position]}")
            ### Go to next gap
            case '+':        
                clear_screen()
                first_run = False 
                if current_gap_position_idx + 1 == len(gap_positions):
                    current_gap_position_idx -= 1
                    print("You already reached the end of the text.")
        
                current_gap_position_idx += 1
                current_gap_position = gap_positions[current_gap_position_idx]
                
                print(f"\n\n{splitted_gap_text[current_gap_position]}")
            ### Go to main menu
            case 'q':
                return
            ### Ask Gemini for a hint
            case 'h':
                print("Function not yet available.")
                input("Press Enter to continue.")
            ### Reprompts until an input is given that is accepted
            case _:
                users_solution = next_action
                #### Evaluate the provided result
                if users_solution == "Test":
                    print("Good job!")
                    print("Let's proceed to the next gap.")
                    pass
                else:
                    print("Try again.")
                input("Press Enter to continue.")


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
        app_context["text_file_path"] = input("Please enter your text file path.\nFor instance: 'data/project-gutenberg/sample_text_file.txt'\n")
    
    separator_equalsign_50()
    print(f"Your current text file is:\n{app_context['text_file_path']}")
    separator_equalsign_50()
    
    # Change the input if desired
    change_source = input("If you want to change the source, please press 1. Otherwise press any key.\n")
    if change_source == '1':
        app_context["text_file_path"] = input("Please enter your new text file path.\n")
        
    # Generate a preview of the first 5 lines
    separator_equalsign_50()
    print("Preview of the selected text:")
    pass
    separator_equalsign_50()


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

