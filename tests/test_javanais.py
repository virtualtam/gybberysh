"""Test Javanais text conversion"""
from gybberysh.games import javanais


def test_empty_text():
    """Thanks for nothing!"""
    assert javanais("") == ""
    assert javanais(None) == ""
    assert javanais([]) == ""


def test_simple_word():
    """Convert simple words to Javanais"""
    assert javanais("gros") == "gravos"
    assert javanais("pesto") == "pavestavo"
    assert javanais("Bon") == "Bavon"
    assert javanais("Plans") == "Plavans"
    assert javanais("Supermarché") == "Savupavermavarchavé"


def test_consecutive_vowels():
    """Convert words containing consecutive vowels"""
    assert javanais("bonjour") == "bavonjavour"
    assert javanais("train") == "travain"


def test_y_as_consonant():
    """Treat 'y' as a consonant when it precedes a vowel"""
    assert javanais("coyote") == "cavoyavote"
    assert javanais("Coyotes.") == "Cavoyavotes."


def test_first_capital_vowel():
    """Capitalize the beginning of a converted word"""
    assert javanais("Ô") == "Avô"
    assert javanais("I can has?") == "Avi cavan havas?"
    assert javanais("Allô Ola Nabila") == "Avallavô Avolava Navabavilava"


def test_final_silent_e():
    """Do not insert <infix> before a final -e / -es"""
    assert javanais("betterave") == "bavettaveravave"
    assert javanais("allumettes") == "avallavumavettes"


def test_postfix_qu():
    """Insert <infix> after 'qu', not between 'q' and 'u'"""
    assert javanais("qualitāy") == "quavalavitavāy"
    assert javanais("Burger Quizz") == "Bavurgaver Quavizz"


def test_convert_sentence():
    """Convert full sentences to Javanais"""
    assert javanais("Jésus Christ") == "Javésavus Chravist"
    assert javanais("Don Quichotte") == "Davon Quavichavotte"
