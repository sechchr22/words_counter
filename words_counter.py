# Show every word in alphabetical order
# And the frequency

# Pseudo
# 1. Open the file
# 2. Extract the words
# 3. Build a dictionary with word as key and the ocurrence as a value
# 4. Sort the dictionary alphabetically
# 5. Print every key - value combination

# Send it to jlromano@intelepeer.ai

import os
import re
from collections import Counter

# Define the base directory and input file path
BASE_DIR = os.path.dirname(__file__)
FILE = os.path.join(BASE_DIR, 'input.txt')

def read_file(file: str):
    """
    Generator that reads a file line by line.

    Args:
        file (str): Path to the input text file.

    Yields:
        str: Each line of the file as a string.

    Notes:
        This approach is memory-efficient and suitable for large files.
    """
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            yield line

def tokenize(line: str):
    """
    Extracts lowercase words from a line of text, ignoring punctuation.

    Args:
        line (str): A line of text.

    Returns:
        List[str]: A list of cleaned, lowercase words.
    """
    return [word.lower() for word in re.findall(r'\b\w+\b', line)]

def count_words(lines):
    """
    Counts word occurrences across multiple lines.

    Args:
        lines (Iterable[str]): Lines of text.

    Returns:
        Counter: A dictionary-like object with word frequencies.
    """
    counter = Counter()
    for line in lines:
        counter.update(tokenize(line))
    return counter

def print_word_counts(counter: Counter):
    """
    Prints word counts sorted alphabetically.

    Args:
        counter (Counter): Word frequency dictionary.
    """
    for word, occurrence in sorted(counter.items()):
        print(f"{word}: {occurrence}")

if __name__ == "__main__":
    lines = read_file(FILE)
    word_counts = count_words(lines)
    print_word_counts(word_counts)