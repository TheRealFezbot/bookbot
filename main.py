import sys
from stats import number_of_words, character_number, list_of_dicts

# protect from user errors
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# get the book text from filepath

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    
    character_count = character_number(book_text)
    sorted_list = list_of_dicts(character_count)
    
    # Output
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    number_of_words(book_text)
    print("--------- Character Count -------")

    for char in sorted_list:
        print(f"{char['char']}: {char['num']}")
    
    print("============= END ===============")

main()