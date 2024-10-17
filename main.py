import re

"""Module providing a function printing python version."""

FILE_PATH = "books/frankenstein.txt"


def count_words(string: str):
    """counts words in a passed in string"""
    words = string.split()
    total_words = len(words)
    return total_words


def count_characters(string: str) -> dict[str, int]:
    """gets a count of all characters within a given string"""
    string_lower = string.lower()
    removed_chars = re.sub("[^a-z]+", "", string_lower)
    chars = list(removed_chars)
    chars_count: dict[str, int] = {}
    for char in chars:
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


def print_report(file_path: str):
    """print to the console a report of data about a given text file"""
    book_text = get_file_contents(file_path)
    book_words = count_words(book_text)
    book_character_count = count_characters(book_text)
    sorted_charater_count = dict(
        sorted(book_character_count.items(), key=lambda item: item[1], reverse=True)
    )

    print(f"--- Begin report of {FILE_PATH} ---")
    print(f"{book_words} words found in the document")
    for character, count in sorted_charater_count.items():
        plural_string = "" if count == 1 else "s"
        print(f"The '{character} character was found {count} time{plural_string}")

    print("--- End report ---")


print_report(FILE_PATH)
