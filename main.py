def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(text):
    word_list = text.split()
    return len(word_list)


main()
