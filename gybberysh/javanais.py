"""Javanais

Basic rules:
- <infix> is inserted after each group of consonants that is followed by a vowel
- if a word starts with a vowel, <infix> is inserted before this vowel

Extended rules:
- 'qu' is kept for syntactic purposes
  "query" => "quaveravy"
- the final '-e/-es' is not infixed
  "tarte" => "tavarte"
- 'y' behaves as a consonant when it is followed by a vowel
  "coyote" => "cavoyavote"
"""
import argparse
import re

from .utils import is_consonant, is_vowel

JAVANAIS_INFIX = "av"
INFIXES = [JAVANAIS_INFIX, "ab", "ad", "al"]


def infix_word(word, infix):
    """Infix a single word with a given syllable"""
    previous = ""
    new_word = ""

    for index, char in enumerate(word):
        if (previous.lower(), char.lower()) == ('q', 'u'):
            new_word += char + infix

        elif (word[index:].lower() in ('e', 'es') and
              (is_consonant(previous) or
               previous.lower() == 'y')):
            new_word += char

        elif (is_vowel(char) and
              (index == 0 or
               is_consonant(previous) or
               previous.lower() == 'y')):
            if char.isupper():
                new_word += infix.capitalize() + char.lower()
            else:
                new_word += infix + char

        else:
            new_word += char

        previous = char

    return new_word


def infix_text(text, infix):
    """Infix text with a given syllable"""
    if not text:
        return ""

    new_text = []

    for token in text.split():
        new_token = ""

        for subtoken in re.findall(r"\w+|[^\w\s]", token):
            new_token += infix_word(subtoken, infix)

        new_text.append(new_token)

    return " ".join(new_text)


def javanais(text, infix=JAVANAIS_INFIX):
    """Convert text to Javanais"""
    return infix_text(text, infix)


def main():
    """Main entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'text',
        type=str,
        nargs='+',
        help="text to convert to Javanais"
    )
    parser.add_argument(
        '-i',
        '--infix',
        type=str,
        choices=INFIXES,
        default=JAVANAIS_INFIX,
        help="infixed syllable"
    )
    args = parser.parse_args()
    print(infix_text(" ".join(args.text), args.infix))
