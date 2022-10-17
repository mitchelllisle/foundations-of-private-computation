import pytest

from privcomp import MonoAlphabeticCipher, ShiftCipher, ShiftCipherAttack, VigenereCipher
from privcomp.ciphers.cipher import AbstractCipher


@pytest.fixture
def shift_cipher() -> ShiftCipher:
    sc = ShiftCipher()
    return sc


@pytest.fixture
def vigenere_cipher() -> VigenereCipher:
    c = VigenereCipher()
    return c


@pytest.fixture
def shift_cipher_attack(shift_cipher_text) -> ShiftCipherAttack:
    sc = ShiftCipherAttack(shift_cipher_text)
    return sc


@pytest.fixture
def plaintext() -> str:
    djo_lyrics = """
    I need to walk my dog Im ready to go
    My dogs expecting me Im ready to go
    I hate this temperature Im ready to go
    This music sucks to me Im ready to go
    """
    return AbstractCipher.clean_text(djo_lyrics)


@pytest.fixture
def shift_cipher_text() -> str:
    cipher = """
    l qhhg wr zdon pb grj lp uhdgb wr jr
    pb grjv hashfwlqj ph lp uhdgb wr jr
    l kdwh wklv whpshudwxuh lp uhdgb wr jr
    wklv pxvlf vxfnv wr ph lp uhdgb wr jr
    """
    return AbstractCipher.clean_text(cipher)


@pytest.fixture
def mono_alphabetic_cipher_text() -> str:
    cipher = """
    i fnnc oe wxvy mh ceb im anxch oe be
    mh cebg nqsnkoifb mn im anxch oe be
    i jxon ojig onmsnaxouan im anxch oe be
    ojig mugik gukyg oe mn im anxch oe be
    """
    return AbstractCipher.clean_text(cipher)


@pytest.fixture
def vigenere_cipher_text() -> str:
    cipher = """
    r snwi lt ofuc vq mgl ar jjjvd lt yt
    ed vtpk npunuyrfl ej ar jjjvd lt yt
    a qsyn yqax ljvhjasydjj ar jjjvd lt yt 
    lmrk vmxru bmhtk cg vw re awfmq cg pg
    """
    return AbstractCipher.clean_text(cipher)


@pytest.fixture
def mono_alphabetic_cipher() -> MonoAlphabeticCipher:
    cipher = MonoAlphabeticCipher()
    return cipher
