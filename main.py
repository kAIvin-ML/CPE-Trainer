import sys
from utils import file_path_provided
from data_handler import get_text_from_file


def main():
    if file_path_provided(sys.argv):
        text_path = sys.argv[1]
    else:
        raise Exception("Please try again by providing a file path.")
    text = get_text_from_file(text_path)
    print("==========BEGIN=========")
    print(text)
    print("=========END=========")

if __name__ == "__main__":
    main()
