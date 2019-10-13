"""Language games"""
import argparse

from .infix import infix_text

GIBBERISH = "iddig"
JAVANAIS = "av"
OPPISH = "op"
INFIXES = [JAVANAIS, "ab", "ad", "al", OPPISH]

UPSIDOWN = [
    ("a", "g"),
    ("b", "p"),
    ("d", "q"),
    ("f", "t"),
    ("m", "w"),
    ("n", "u"),
    ("s", "z"),
    ("A", "V"),
    ("M", "W"),
    ("S", "Z"),
]


def gibberish(text):
    """Convert text to Gibberish"""
    return infix_text(text, GIBBERISH)


def javanais(text):
    """Convert text to Javanais

    See:
    - https://en.wikipedia.org/wiki/Javanais
    - https://fr.wikipedia.org/wiki/Javanais_(argot)
    """
    return infix_text(text, JAVANAIS)


def oppish(text):
    """Oppish Gangnam Style!!!

    See:
    - http://www.wikihow.com/Speak-Oppish
    - http://www.wikihow.com/Sample/Oppish-Words
    """
    return infix_text(text, OPPISH)


def upsidown(text):
    """Turn letters upside-down"""
    if not text:
        return ""

    uptext = ""

    for char in text:
        upchar = char

        for ch1, ch2 in UPSIDOWN:
            if char == ch1:
                upchar = ch2
                break
            if char == ch2:
                upchar = ch1
                break

        uptext += upchar

    return uptext


def gibberish_entrypoint():
    """Gibberish entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "text", type=str, nargs="+", help="text to convert to Gibberish"
    )
    args = parser.parse_args()
    print(gibberish(" ".join(args.text)))


def javanais_entrypoint():
    """Javanais entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, nargs="+", help="text to convert to Javanais")
    args = parser.parse_args()
    print(javanais(" ".join(args.text)))


def upsidown_entrypoint():
    """Miwwow entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, nargs="+", help="text to upsidown")
    args = parser.parse_args()
    print(upsidown(" ".join(args.text)))


def oppish_entrypoint():
    """Oppish entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, nargs="+", help="text to convert to Oppish")
    args = parser.parse_args()
    print(oppish(" ".join(args.text)))


def generic_infix_entrypoint():
    """Infix entrypoint for custom infix usage"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "text", type=str, nargs="+", help="text to convert using an infixed syllable"
    )
    parser.add_argument(
        "-i",
        "--infix",
        type=str,
        choices=INFIXES,
        default=OPPISH,
        help="infixed syllable",
    )
    args = parser.parse_args()
    print(infix_text(" ".join(args.text), args.infix))
