"""Language games"""
import argparse

from .infix import infix_text

JAVANAIS = "av"
OPPISH = "op"
INFIXES = [JAVANAIS, "ab", "ad", "al", OPPISH]


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


def javanais_entrypoint():
    """Javanais entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'text',
        type=str,
        nargs='+',
        help="text to convert to Javanais"
    )
    args = parser.parse_args()
    print(javanais(" ".join(args.text)))


def oppish_entrypoint():
    """Oppish entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'text',
        type=str,
        nargs='+',
        help="text to convert to Javanais"
    )
    args = parser.parse_args()
    print(oppish(" ".join(args.text)))


def generic_infix_entrypoint():
    """Infix entrypoint for custom infix usage"""
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
        default=OPPISH,
        help="infixed syllable"
    )
    args = parser.parse_args()
    print(infix_text(" ".join(args.text), args.infix))
