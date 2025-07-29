from stats import get_num_words
from stats import get_num_characters
from stats import create_sorted_list
import sys

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_dict = get_num_characters(text)
        sorted_list = create_sorted_list(char_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_list:
            if item['char'].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()