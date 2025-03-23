def num_of_words(contents):
    num_words = len(contents.split())
    print(f"{num_words} words found in the document")

def number_of_characters(contents):
    contents = contents.lower()
    dictionary = {}
    for character in contents:
        dictionary[character] = dictionary.get(character, 0) + 1
    print(dictionary)