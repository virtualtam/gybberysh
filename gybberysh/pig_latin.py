"""Pig Latin

Basic rules:
- words starting with a vowel are suffixed by 'yay'
- for words starting with a consonant:
  - the first consonant cluster is moved at the end of the word
  - the word is then suffixed by 'ay'

Extended rules:
- 'qu' is kept for syntactic purposes
  "query" => "ery-qu-ay"
- 'y' behaves as a consonant when it is followed by a vowel
  "you" => "ou-y-ay"

Additional notes:
- some conversions are ambiguous (unless explicited with hyphens):
  - "ear" => "ear-yay"
  - "year" => "ear-y-ay"
"""
import argparse
import re

from .utils import is_vowel

SHORT_SUFFIX = "ay"
LONG_SUFFIX = "yay"


def pig_latin_word(word):
    """Converts a single word to Pig Latin"""
    if not word:
        return LONG_SUFFIX.capitalize + "!"

    new_word = ""

    if len(word) > 1 and word[0].lower() == "y" and is_vowel(word[1]):
        new_word = word[1:] + LONG_SUFFIX

    elif is_vowel(word[0]):
        new_word = word + LONG_SUFFIX

    elif word.startswith("qu"):
        new_word = word[2:] + "qu" + SHORT_SUFFIX

    else:
        previous = ""

        for index, char in enumerate(word):
            if (previous, char) == ("q", "u"):
                new_word = word[index + 1 :] + word[: index + 1] + SHORT_SUFFIX
                break

            if is_vowel(char):
                new_word = word[index:] + word[:index] + SHORT_SUFFIX
                break

            previous = char

    if word[0].isupper():
        return new_word.capitalize()

    return new_word


def pig_latin(text):
    """Converts text to Pig Latin"""
    if not text:
        return "{}!".format(LONG_SUFFIX.capitalize())

    new_text = []

    for token in text.split():
        new_token = ""

        for subtoken in re.findall(r"\w+|[^\w\s]", token):
            new_token += pig_latin_word(subtoken)

        new_text.append(new_token)

    return " ".join(new_text)


def pig_latin_entrypoint():
    """Pig Latin entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "text", type=str, nargs="+", help="text to convert to Pig Latin"
    )
    args = parser.parse_args()
    print(pig_latin(" ".join(args.text)))
