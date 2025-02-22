from stats import num_words
from stats import char_count
from stats import get_sorted_dict_list
import sys

def main() -> int:
    #get_book_text('books/frankenstein.txt')

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    num_words(get_book_text(sys.argv[1]))
    my_dict = char_count(get_book_text(sys.argv[1]))

   # for k, v in my_dict.items():
    #    print(f"'{k}': {v}")

    my_list = get_sorted_dict_list(my_dict)

    for item in my_list:
        for k, v in item.items():
            print(f"{k}: {v}")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents



main()