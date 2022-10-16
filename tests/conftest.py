import pytest

from privcomp import ShiftCipher


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
def ciphertext() -> str:
    cipher = """
    l qhhg wr zdon pb grj lp uhdgb wr jr
    pb grjv hashfwlqj ph lp uhdgb wr jr
    l kdwh wklv whpshudwxuh lp uhdgb wr jr
    wklv pxvlf vxfnv wr ph lp uhdgb wr jr
    """
    return cipher
