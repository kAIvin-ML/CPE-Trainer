import sys
from utils import file_path_provided, is_not_empty_txt
from data_handler import get_text_from_file


def main():

    # Load a text file
    if file_path_provided(sys.argv) and is_not_empty_txt(sys.argv[1]):
        text_path = sys.argv[1]
    text = get_text_from_file(text_path)
    
    # Output the content given
    print("==========BEGIN=========")
    print(text)
    print("=========END=========")


if __name__ == "__main__":
    main()
