from stats import number_of_words, character_number

# get the book text from filepath

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    number_of_words(book_text)
    character_count = character_number(book_text)
    print(character_count)

main()