def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def get_num_words(book):
    return len(book.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts