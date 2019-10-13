#!/usr/bin/env python3
"""Setup script for gybberysh"""
import codecs
import os
import re

from setuptools import find_packages, setup


def get_long_description():
    """Reads the main README.rst to get the program's long description"""
    with codecs.open("README.rst", "r", "utf-8") as f_readme:
        return f_readme.read()


def get_program_metadata(attribute):
    """Reads program metadata from the main package's __init__"""
    with open(os.path.join("gybberysh", "__init__.py"), "r") as f_init:
        return re.search(
            r'^__{attr}__\s*=\s*[\'"]([^\'"]*)[\'"]'.format(attr=attribute),
            f_init.read(),
            re.MULTILINE,
        ).group(1)


setup(
    name=get_program_metadata("title"),
    version=get_program_metadata("version"),
    description="Gibberish, pig latin and other language games",
    long_description=get_long_description(),
    author=get_program_metadata("author"),
    author_email="virtualtam@flibidi.net",
    license="MIT",
    url="https://github.com/virtualtam/gybberysh",
    keywords="gibberish pig latin slang javanais largonji",
    packages=find_packages(exclude=["tests.*", "tests"]),
    entry_points={
        "console_scripts": [
            "bofh = gybberysh.bofh:main",
            "gibberish = gybberysh.games:gibberish_entrypoint",
            "infix = gybberysh.games:generic_infix_entrypoint",
            "javanais = gybberysh.games:javanais_entrypoint",
            "upsidown = gybberysh.games:upsidown_entrypoint",
            "oppish = gybberysh.games:oppish_entrypoint",
            "piglatin = gybberysh.pig_latin:pig_latin_entrypoint",
        ]
    },
    install_requires=[],
    extras_require={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
