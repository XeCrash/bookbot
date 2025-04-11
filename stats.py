def get_num_words(book_text: str):
    """This function takes a books text and returns the number of words in the book.
    
    Args:
        book_text (str): The book object's text
        
    Return: 
        The number of words in the book
    """
    num_words = len(book_text.split())
    return num_words

def get_each_char_count(book_text: str, isalpha_filter = False):
    """This provides a way to count all char's, symbols, and spaces

    Args:
        book_text (str): the book object's text
        isalpha_filter (bool): ability to filter for only .isalpha() characters 
        
    Return:
        char_count (dict): A new dict containing counts for all referenced characters, symbols, and spaces
    """
    char_count = {}
    lower_case_text = book_text.lower()
    for char in lower_case_text:
        if isalpha_filter == True:
            if char not in char_count and char.isalpha() == True: # char is new and non-special char
                char_count[char] = 1
            elif char in char_count and char.isalpha() == True:
                char_count[char] += 1
        else:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count  

def sort_chars_to_list(chars: dict):
    """_summary_

    Args:
        chars (dict): _description_

    Returns:
        list[tuple]: _description_
    """
    list_of_chars = list(chars.items())
    list_of_chars.sort()
    return list_of_chars
