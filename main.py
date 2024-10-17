"""Module providing a function printing python version."""

FILE_NAME = "./books/frankenstein.txt"


def count_words(string: str):
    """counts words in a passed in string"""
    words = string.split()
    total_words = len(words)
    return total_words


def count_characters(string: str) -> dict[str, int]:
    """gets a count of all characters within a given string"""
    removed_chars = string.lower().replace("\n", "").replace(" ", "")
    chars = list(removed_chars)
    chars_count: dict[str, int] = {}
    for char in chars:
        print(char)
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count


# Open the file and read its content.
with open(FILE_NAME, encoding="utf-8") as f:
    file_content = f.read()

book_words = count_words(file_content)

print(book_words)
print(count_characters(file_content))
