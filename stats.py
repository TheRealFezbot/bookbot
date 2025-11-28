def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}

    for character in text.lower():
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    sorted = []
    for key in dict:
        sorted.append({"char": key, "num": dict[key]})
    sorted.sort(reverse=True, key=sort_on)
    
    return sorted