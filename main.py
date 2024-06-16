def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    print_report(num_words, character_count(text))

def get_book_text(file_path):
    # reads text and returns it
    with open(file_path) as f:
        return f.read()


def word_count(text):
    # splits text into list where the element of list is each word
    word_list = text.split()
    return len(word_list)


def character_count(text):
    # sets all chars to lower case
    text = text.lower()
    char_count = {}
    # adds chars to char_count as a key and counts num of occurrences of each char as the value
    for char in text:
        if char not in char_count.keys():
            char_count[char] = 1
        elif char in char_count.keys():
            char_count[char] += 1
    return char_count


def sort_on(dict):
    # support function to help sort function know what to sort by
    return dict["num"]


def print_report(num_of_words, char_count):

    char_list = []

    # checks if char is alpha and store char and occurrences in separate dict and adds it to char_list
    for char in char_count:
        if char.isalpha():
            char_list.append({"char": char, "num": char_count[char]})

    # sorts the list of dicts by the char with most occurrences to the char with the least occurrences
    char_list.sort(reverse=True, key=sort_on)

    # report layout *this prints the report to the console*
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_of_words} words found in the document\n")

    for i in range(len(char_list)):
        print(f"The '{char_list[i]['char']}' character was found {char_list[i]['num']} times")

    print("--- End report ---")

main()
