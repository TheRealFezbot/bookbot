
# split the text into a list of words and count the words

def number_of_words(book_text):
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document")

# count each character

def character_number(book_text):
    character_count = {}
    for char in book_text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    print(character_count)