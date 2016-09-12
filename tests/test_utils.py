"""Test text processing utilities"""
from gybberysh.utils import is_consonant, is_consonant_or_y, is_vowel


def test_ascii_is_consonant():
    """Check if an ASCII letter is a consonant"""
    assert is_consonant('b')
    assert is_consonant('c')
    assert is_consonant('d')
    assert is_consonant('f')
    assert is_consonant('g')
    assert is_consonant('h')
    assert is_consonant('j')
    assert is_consonant('k')
    assert is_consonant('l')
    assert is_consonant('m')
    assert is_consonant('n')
    assert is_consonant('p')
    assert is_consonant('q')
    assert is_consonant('r')
    assert is_consonant('s')
    assert is_consonant('t')
    assert is_consonant('v')
    assert is_consonant('w')
    assert is_consonant('x')
    assert is_consonant('z')


def test_accented_is_consonant():
    """Check if an accented letter is a consonant"""
    assert is_consonant('ñ')
    assert is_consonant('ś')


def test_ascii_is_consonant_or_y():
    """Check if an ASCII letter is a consonantor a 'y'"""
    assert is_consonant_or_y('m')
    assert is_consonant_or_y('n')
    assert is_consonant_or_y('Y')
    assert is_consonant_or_y('y')


def test_ascii_is_vowel():
    """Check if an ASCII letter is a vowel"""
    assert is_vowel('a')
    assert is_vowel('e')
    assert is_vowel('i')
    assert is_vowel('o')
    assert is_vowel('u')
    assert is_vowel('y')


def test_accented_is_vowel():
    """Check if an accented letter is a vowel"""
    assert is_vowel('ä')
    assert is_vowel('â')
    assert is_vowel('à')
    assert is_vowel('å')
    assert is_vowel('é')
    assert is_vowel('è')
    assert is_vowel('ë')
    assert is_vowel('ê')
    assert is_vowel('ï')
    assert is_vowel('î')
    assert is_vowel('ī')
    assert is_vowel('ö')
    assert is_vowel('ù')


def test_undetected_accented_vowel():
    """Edge vowel cases"""
    assert not is_vowel('æ')
    assert not is_vowel('œ')
    assert not is_vowel('ø')
