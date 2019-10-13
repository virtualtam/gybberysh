"""Test Pig Latin text conversion"""
from gybberysh.pig_latin import pig_latin


def test_empty_text():
    """Thanks for nothing!"""
    assert pig_latin("") == "Yay!"
    assert pig_latin(None) == "Yay!"
    assert pig_latin([]) == "Yay!"


def test_simple_word():
    """Convert simple words to Pig Latin"""
    assert pig_latin("box") == "oxbay"
    assert pig_latin("lab") == "ablay"
    assert pig_latin("mice") == "icemay"
    assert pig_latin("nay") == "aynay"
    assert pig_latin("owl") == "owlyay"
    assert pig_latin("query") == "eryquay"


def test_starting_consonants():
    """Words starting with a series of consonants"""
    assert pig_latin("sphere") == "eresphay"
    assert pig_latin("string") == "ingstray"


def test_y_as_consonant():
    """Treat 'y' as a consonant when it precedes a vowel"""
    assert pig_latin("you") == "ouyay"
    assert pig_latin("year") == "earyay"
    assert pig_latin("ear") == "earyay"


def test_qu():
    """Keep "qu" for syntactic purposes"""
    assert pig_latin("quality") == "alityquay"
    assert pig_latin("Squirrel") == "Irrelsquay"


def test_convert_sentence():
    """Pig latinize full sentences"""
    assert (
        pig_latin("The quick brown fox jumps over the lazy dog")
        == "Ethay ickquay ownbray oxfay umpsjay overyay ethay azylay ogday"
    )
