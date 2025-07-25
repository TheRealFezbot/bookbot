
# split the text into a list of words and count the words

def number_of_words(book_text):
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

# count each character

def character_number(book_text):
    character_count = {}
    for char in book_text.lower():
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count

def sort_on(items):
    return items["num"]


def list_of_dicts(dict):
    dict_list = []
    list_of_dict = dict.items()
    for items in list_of_dict:
        new_dict = {}
        new_dict["char"] = items[0]
        new_dict["num"] = items[1]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    
