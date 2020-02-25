#!/usr/bin/env python3
"""Star Wars Spoiler Generator

https://xkcd.com/2243/
"""
import random

VILLAIN = [
    "Kyle Ren",
    "Malloc",
    "Darth Sebelius",
    "Theranos",
    "Lord Juul",
]

FRIEND = [
    "Kim Spacemeasurer",
    "Teen Yoda",
    "Dab Tweetdeck",
    "Yaz Progestin",
    "TI-83",
]

LIGHTSABER_COLOR = [
    "aquamarine",
    "beige",
    "ochre",
    "mauve",
    "taupe",
]

SUPERWEAPON = [
    "Sun Obliterator",
    "Moonsquisher",
    "World Eater",
    "Planet Zester",
    "Superconducting Supercollider",
]

SUPERWEAPON_POWER = [
    "blowing up a planet with a bunch of beams of energy that combine into one",
    "blowing up a bunch of planets with a beam of energy that splits into many",
    "cutting a planet in halves and smashing the halves together like two cymbals",
    "increasing the CO2 levels in a planet's atmosphere, causing rapid heating",
    "triggering the en credits before the movie is done",
]

ENEMY = [
    "Boba Fett",
    "Salacious Crumb",
    "The Space Slug",
    "the bottom half of Darth Maul",
    "Youtube commenters",
]

FEAT = [
    "a bow that shoots little lightsaber-headed arrows",
    "X-Wings and Tie Fighters dodging the giant letters of the opening crawl",
    "a Sith educational display that uses Force lighting to demonstrate the"
    " dielectric breakdown of air",
    "Kylo Ren putting on a helmet over his smaller one",
    "a Sith car wash where the bristles on the brushes are little lightsabers",
]

PARENT_1 = [
    "Luke",
    "Leia",
    "Han",
    "Obi-Wan",
    "a random junk trader",
]

PARENT_2 = [
    "Poe",
    "BB-8",
    "Amilyn Holdo",
    "Laura Dern",
    "a random junk trader",
    "that one droid from the Jawa sandcrawler that says Gonk",
]

TEMPLATE = (
    "In this Star Wars Movie, our heroes return to take on the First Order"
    " and new villain {villain} with help from their new friend {friend}."
    " Rey builds a new lightsaber with a {lightsaber_color} blade, and they"
    " head out to confront the First Order's new superweapon, the {superweapon},"
    " a space station capable of {superweapon_power}. They unexpectedly join"
    " forces with their old enemy, {enemy}, and destroy the superweapon in a battle"
    " featuring {feat}. P.S. Rey's parents are {parent1} and {parent2}"
)


def spoiler():
    """Generate a random Star Wars spoiler"""
    return TEMPLATE.format(
        villain=random.choice(VILLAIN),
        friend=random.choice(FRIEND),
        lightsaber_color=random.choice(LIGHTSABER_COLOR),
        superweapon=random.choice(SUPERWEAPON),
        superweapon_power=random.choice(SUPERWEAPON_POWER),
        enemy=random.choice(ENEMY),
        feat=random.choice(FEAT),
        parent1=random.choice(PARENT_1),
        parent2=random.choice(PARENT_2),
    )


def main():
    """Console entrypoint"""
    print(spoiler())
