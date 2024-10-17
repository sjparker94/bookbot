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


def get_file_contents(file_path: str) -> str:
    """open and read the contents of a file"""
    with open(file_path, encoding="utf-8") as f:
        file_content = f.read()
    return file_content


book_text = get_file_contents(FILE_NAME)

book_words = count_words(book_text)

print(book_words)
print(count_characters(book_text))
