"""Test Oppish text conversion"""
from gybberysh.games import oppish


def test_empty_text():
    """Thanks for nothing!"""
    assert oppish("") == ""
    assert oppish(None) == ""
    assert oppish([]) == ""


def test_simple_word():
    """Convert simple words to Oppish"""
    assert oppish("Hello") == "Hopellopo"
    assert oppish("Goodbye") == "Gopoodbopye"
    assert oppish("Love") == "Lopove"
    assert oppish("Friend") == "Fropiend"
    assert oppish("America") == "Opamoperopicopa"
    assert oppish("Chair") == "Chopair"
    assert oppish("Sofa") == "Sopofopa"
    assert oppish("Apartment") == "Opapopartmopent"
    assert oppish("Police") == "Popolopice"
    assert oppish("Birthday") == "Bopirthdopay"
    assert oppish("Happy") == "Hopappopy"
    assert oppish("Cat") == "Copat"
    assert oppish("Father") == "Fopathoper"
    assert oppish("Calendar") == "Copalopendopar"
    assert oppish("Automobile") == "Opautopomopobopile"
    assert oppish("Oppish") == "Opoppopish"
    assert oppish("Dinner") == "Dopinnoper"
    assert oppish("River") == "Ropivoper"
    assert oppish("Music") == "Mopusopic"
    assert oppish("Girl") == "Gopirl"
    assert oppish("Fancy") == "Fopancopy"


def test_consecutive_vowels():
    """Convert words containing consecutive vowels"""
    assert oppish("baboon") == "bopabopoon"
    assert oppish("yearly") == "yopearlopy"


def test_y_as_consonant():
    """Treat 'y' as a consonant when it precedes a vowel"""
    assert oppish("coyote") == "copoyopote"
    assert oppish("Coyotes.") == "Copoyopotes."
    assert oppish("You") == "Yopou"


def test_first_capital_vowel():
    """Capitalize the beginning of a converted word"""
    assert oppish("Ô") == "Opô"
    assert oppish("I can has?") == "Opi copan hopas?"
    assert oppish("Allô Ola Nabila") == "Opallopô Opolopa Nopabopilopa"


def test_short_final_silent_e():
    """Process short words"""
    assert oppish("Me") == "Mope"


def test_final_silent_e():
    """Do not insert <infix> before a final -e / -es"""
    assert oppish("abide") == "opabopide"
    assert oppish("slope") == "slopope"


def test_postfix_qu():
    """Insert <infix> after 'qu', not between 'q' and 'u'"""
    assert oppish("qualitāy") == "quopalopitopāy"
    assert oppish("Burger Quizz") == "Bopurgoper Quopizz"


def test_convert_sentence():
    """Convert full sentences to Oppish"""
    assert oppish("Jesus Christ") == "Jopesopus Chropist"
    assert oppish("Don Quixote") == "Dopon Quopixopote"
