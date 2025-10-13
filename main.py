def get_book_text(filepath):
    with open(filepath) as f:
        book = f.read()
    return book

def main():
    book_content = get_book_text("books/frankenstein.txt")
    print(book_content)

if __name__ == "__main__":
    main()