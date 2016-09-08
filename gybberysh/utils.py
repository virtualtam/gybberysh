"""Text processing utilities"""
import unicodedata

CONSONANTS = [unicodedata.normalize('NFKD', char).encode('ascii')
              for char in 'bcdfghjklmnpqrstvwxz']
VOWELS = [unicodedata.normalize('NFKD', char).encode('ascii')
          for char in 'aeiouy']


def normalize_to_ascii(char):
    """Strip a character from its accent and encode it to ASCII"""
    return unicodedata.normalize('NFKD', char).encode('ascii', 'ignore').lower()


def is_consonant(char):
    """Detect if a character is a consonant"""
    return normalize_to_ascii(char) in CONSONANTS


def is_vowel(char):
    """Detect if a character is a vowel"""
    return normalize_to_ascii(char) in VOWELS
