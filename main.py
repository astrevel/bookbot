def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    print(character_count(text))


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def word_count(text):
    word_list = text.split()
    return len(word_list)


def character_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count.keys():
            char_count[char] = 1
        elif char in char_count.keys():
            char_count[char] += 1
    return char_count


main()
