import string

import pytest


def test_default_generate(vigenere_cipher):
    key = vigenere_cipher.generate()
    assert len(set(key)) == 3


def test_size_generate(vigenere_cipher):
    for i in range(len(string.ascii_lowercase)):
        key = vigenere_cipher.generate(i)
        assert len(set(key)) == i


def test_max_size_generate(vigenere_cipher):
    with pytest.raises(ValueError):
        vigenere_cipher.generate(len(string.ascii_lowercase) + 1)


def test_encrypt(vigenere_cipher, plaintext):
    encrypted = vigenere_cipher.encrypt(plaintext)
    assert encrypted != plaintext


def test_decrypt(vigenere_cipher, plaintext, vigenere_cipher_text):
    plaintext = vigenere_cipher.clean_text(plaintext)
    t = vigenere_cipher.clean_text(vigenere_cipher_text)
    decrypted = vigenere_cipher.decrypt(t)
    assert plaintext == decrypted


def test_shift_letter(vigenere_cipher):
    for _, letter in enumerate(string.ascii_lowercase):
        shifted = vigenere_cipher._shift_letter(0, letter)
        assert shifted != letter


def test_unshift_letter(vigenere_cipher):
    for letter in string.ascii_lowercase:
        shifted = vigenere_cipher._unshift_letter(0, letter)
        assert shifted != letter
