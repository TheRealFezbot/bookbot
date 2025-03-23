def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def num_of_words(contents):
    num_words = len(contents.split())
    print(f"{num_words} words found in the document")
    
num_of_words(get_book_text("books/frankenstein.txt"))

# def main():
#     print(get_book_text("books/frankenstein.txt"))
    

# main()