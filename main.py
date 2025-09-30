import sys
from stats import get_num_words
from stats import get_letter_frequency
from stats import sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    file_contents = get_book_text(file_path)
    num_words = get_num_words(file_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    letter_frequency = get_letter_frequency(file_contents)
    newer_list = sorted_dictionary(letter_frequency)
    for item in newer_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")





main()
