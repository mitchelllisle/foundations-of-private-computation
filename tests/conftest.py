import pytest

from privcomp import MonoAlphabeticCipher, ShiftCipher


@pytest.fixture
def shift_cipher() -> ShiftCipher:
    sc = ShiftCipher()
    return sc


@pytest.fixture
def plaintext() -> str:
    djo_lyrics = """
    I need to walk my dog Im ready to go
    My dogs expecting me Im ready to go
    I hate this temperature Im ready to go
    This music sucks to me Im ready to go
    """
    return djo_lyrics.lower()


@pytest.fixture
def shift_cipher_text() -> str:
    cipher = """
    l qhhg wr zdon pb grj lp uhdgb wr jr
    pb grjv hashfwlqj ph lp uhdgb wr jr
    l kdwh wklv whpshudwxuh lp uhdgb wr jr
    wklv pxvlf vxfnv wr ph lp uhdgb wr jr
    """
    return cipher


@pytest.fixture
def mono_alphabetic_cipher_text() -> str:
    cipher = """
    i fnnc oe wxvy mh ceb im anxch oe be
    mh cebg nqsnkoifb mn im anxch oe be
    i jxon ojig onmsnaxouan im anxch oe be
    ojig mugik gukyg oe mn im anxch oe be
    """
    return cipher


@pytest.fixture
def mono_alphabetic_cipher() -> MonoAlphabeticCipher:
    cipher = MonoAlphabeticCipher()
    return cipher
