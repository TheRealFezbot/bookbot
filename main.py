
# import stats.py
from stats import get_book_text, num_of_words, number_of_characters, sort_character_count, print_report

# variables
path = "books/frankenstein.txt"
word_count = num_of_words(get_book_text(path))
char_counts = number_of_characters(get_book_text(path))
sorted_chars = sort_character_count(char_counts)

#print the report
print_report(path, word_count, sorted_chars)