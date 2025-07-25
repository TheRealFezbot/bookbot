def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def number_of_words(book_text):
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document")

def main():
    book_text = get_book_text("books/frankenstein.txt")
    number_of_words(book_text)

main()