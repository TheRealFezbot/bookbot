def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import num_of_words
from stats import number_of_characters

num_of_words(get_book_text("books/frankenstein.txt"))
number_of_characters(get_book_text("books/frankenstein.txt"))

# def main():
#     print(get_book_text("books/frankenstein.txt"))
    

# main()