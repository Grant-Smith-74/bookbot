from stats import get_num_words, get_book_text, count_characters

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book_content)} total words")
    char_freq = count_characters(book_content)
    print("\nCharacter frequencies:")
    for char, freq in sorted(char_freq.items()):
        print(f"'{char}': {freq}")

if __name__ == "__main__":
    main()