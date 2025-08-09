from data_handler import get_text_from_file
from menu_items import display_text, display_mc_lexical_cloze, display_open_cloze, display_word_formation, display_key_word_transformation, analyze_speech, view_settings, exit_app, display_menu
from text_functionality import call_choice
from presentation import clear_screen


def main():
    # Initial settings for the app to run
    app_context = {
        "is_running": True,
        "current_text": None,
        "current_gap_text": None,
        "current_gap": 0,
        "text_file_path": "texts/project-gutenberg/sample_text_file.txt" #None
    }

    # For testing purposes: loads a text to the context dict
    text = get_text_from_file(app_context["text_file_path"])
    app_context["current_text"] = text

    # Run the app
    while app_context["is_running"]:
        # Prepare the menu
        clear_screen()
        display_menu()

        # Run the exercise the user selected
        choice = input("Please enter your choice by entering the corresponding number: ")
        match choice:
            ## Displays text as is
            case '1':
                call_choice(app_context, choice, display_text)
            ## Displays reading exercises
            case '2':
                call_choice(app_context, choice, display_mc_lexical_cloze)
            case '3':
                call_choice(app_context, choice, display_open_cloze)
            case '4':
                call_choice(app_context, choice, display_word_formation)
            case '5':
                call_choice(app_context, choice, display_key_word_transformation)
            ## Analyze speech
            case '6':
                call_choice(app_context, choice, analyze_speech)
            ## System functions
            case '8':
                call_choice(app_context, choice, view_settings)
            case '9':
                call_choice(app_context, choice, exit_app)
            ## Capture all other events
            case _:
                print("Invalid choice. Please enter a number from the menu.")
                input("\nPress Enter to continue...")
                continue

        # 'Pauses' the app after a selection
        if app_context["is_running"]:
            input(">>> Press Enter to display the menu again. <<<")


if __name__ == "__main__":
    main()