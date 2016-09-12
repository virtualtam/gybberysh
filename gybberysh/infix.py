"""Tools for infix-based language games

Basic rules:
- <infix> is inserted after each group of consonants that is followed by a vowel
- if a word starts with a vowel, <infix> is inserted before this vowel

Extended rules:
- 'qu' is kept for syntactic purposes
  "query" => "quaveravy"
- for 3+ character words, the final '-e/-es' is not infixed
  "abide" => "avabavide"
- 'y' behaves as a consonant when it is followed by a vowel
  "coyote" => "cavoyavote"
"""
import re

from .utils import is_consonant_or_y, is_vowel


def infix_word(word, infix):
    """Infix a single word with a given syllable"""
    previous = ""
    new_word = ""

    for index, char in enumerate(word):
        if (previous.lower(), char.lower()) == ('q', 'u'):
            new_word += char + infix

        elif (len(word) > 2 and
              word[index:].lower() in ('e', 'es') and
              is_consonant_or_y(previous)):
            new_word += char

        elif char.lower() == 'y' and index == 0:
            new_word += char

        elif (is_vowel(char) and
              (index == 0 or is_consonant_or_y(previous))):
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
