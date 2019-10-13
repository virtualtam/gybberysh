"""Test Bastard Operator From Hell excuse generation"""
from gybberysh.bofh import ADJECTIVE, LEVEL, NOUN_1, NOUN_2, _bofh, bofh


def test_private_bofh():
    """Undiagnosable Bus Invalidation Flag"""
    excuse = _bofh()

    assert len(excuse) == 4

    adjective, noun1, noun2, level = excuse

    assert adjective in ADJECTIVE
    assert noun1 in NOUN_1
    assert noun2 in NOUN_2
    assert level in LEVEL


def test_public_bofh():
    """Outmoded Loading Corruption Signal"""
    excuse = [w.lower() for w in bofh().split()]

    assert len(excuse) == 4

    adjective, noun1, noun2, level = excuse

    assert adjective in ADJECTIVE
    assert noun1 in NOUN_1
    assert noun2 in NOUN_2
    assert level in LEVEL
