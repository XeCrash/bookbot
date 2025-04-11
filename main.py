import sys
from stats import get_num_words
from stats import get_each_char_count
from stats import sort_chars_to_list

def get_book_text(book: object):
    """
    This function takes a book path and returns the text of the book object.
    :param book: The book object
    :return: The text of the book
    """
    with open(book, 'r') as file:
        book_contents = file.read()
    # Assuming the book object has a text attribute

    return book_contents

def main():
    """
    Main function to run the script.
    """
    test_book_path = "books/frankenstein.txt"  # book path
    if len(sys.argv) == 2:
        argv_path_to_book = sys.argv[1]
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {argv_path_to_book}...")
        print(f"----------- Word Count ----------")
        book_text = get_book_text(argv_path_to_book)
        #print(book_text)  # Print the book text or do something else with it
        print(f"Found {get_num_words(book_text)} total words")
        print(f"--------- Character Count -------")
        char_list = sort_chars_to_list(get_each_char_count(book_text, True))
        #print(f"{get_each_char_count(book_text)}")
        for tup_key, tup_val in char_list:
            print(f"{tup_key}: {tup_val}")
        print(f"============= END ===============")
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
 
main()
