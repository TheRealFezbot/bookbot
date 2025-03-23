# import stats.py and sys
import sys
from stats import get_book_text, num_of_words, number_of_characters, sort_character_count, print_report

# check if a book path was given
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# variables
path = sys.argv[1]
word_count = num_of_words(get_book_text(path))
char_counts = number_of_characters(get_book_text(path))
sorted_chars = sort_character_count(char_counts)


# print the report
print_report(path, word_count, sorted_chars)