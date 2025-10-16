import sys
from stats import get_num_words, get_book_text, count_characters, format_and_sort_char_counts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    print(f"Found {get_num_words(book_content)} total words")
    char_freq = count_characters(book_content)

    for char_info in format_and_sort_char_counts(char_freq):
        print(f"{char_info['char']}: {char_info['num']}")

if __name__ == "__main__":
    main()