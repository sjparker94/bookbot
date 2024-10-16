"""Module providing a function printing python version."""

FILE_NAME = "./books/frankenstein.txt"


def count_words(string: str):
    """counts words in a passed in string"""
    words = string.split()
    total_words = len(words)
    return total_words


# Open the file and read its content.
with open(FILE_NAME, encoding="utf-8") as f:
    file_content = f.read()

book_words = count_words(file_content)

print(book_words)
