"""Test upsidown text conversion"""
from gybberysh.games import upsidown


def test_empty_text():
    """Thanks for nothing!"""
    assert upsidown("") == ""
    assert upsidown(None) == ""
    assert upsidown([]) == ""


def test_simple_word():
    """Turn simple words upsidown"""
    assert upsidown("cow") == "com"
    assert upsidown("break") == "pregk"
    assert upsidown("formats") == "torwgfz"
    assert upsidown("upsidown") == "nbziqomu"


def test_capitalized_word():
    """Turn capitalized words upsidown"""
    assert upsidown("Vale") == "Agle"
    assert upsidown("When") == "Mheu"
