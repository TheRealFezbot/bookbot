# get the book text from the path
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#count the number of words
def num_of_words(contents):
    num_words = len(contents.split())
    return num_words

#count the number of characters
def number_of_characters(contents):
    contents = contents.lower()
    dictionary = {}
    for character in contents:
        dictionary[character] = dictionary.get(character, 0) + 1
    return(dictionary)

#sort the characters
def sort_character_count(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

#print the report 
def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")





