from stats import get_num_words
from stats import count_characters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    char_count_dictionary = count_characters(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    get_num_words(book_path)
    print("--------- Character Count -------")
    for key, value in char_count_dictionary:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

main()
