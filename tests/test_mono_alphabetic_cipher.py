import string


def test_generate(mono_alphabetic_cipher):
    keyspace = mono_alphabetic_cipher.generate()
    assert keyspace != string.ascii_lowercase
    for v in keyspace:
        assert v in string.ascii_lowercase


def test_mono_alphabetic_cipher(mono_alphabetic_cipher):
    assert len(mono_alphabetic_cipher.keyspace) == 26


def test_mono_alphabetic_encrypt(mono_alphabetic_cipher, shift_cipher_plaintext):
    encrypted = mono_alphabetic_cipher.encrypt(shift_cipher_plaintext)
    assert encrypted != shift_cipher_plaintext


def test_mono_alphabetic_decrypt(mono_alphabetic_cipher, shift_cipher_plaintext, mono_alphabetic_cipher_text):
    decrypted = mono_alphabetic_cipher.decrypt(mono_alphabetic_cipher_text)
    assert shift_cipher_plaintext.strip().replace('\n', '') == decrypted


def test_shift_letter(mono_alphabetic_cipher):
    for idx, letter in enumerate(string.ascii_lowercase):
        shifted = mono_alphabetic_cipher._shift_letter(letter)
        assert shifted == mono_alphabetic_cipher.keyspace[idx]


def test_unshift_letter(mono_alphabetic_cipher):
    alphabet_lookup = dict(zip(string.ascii_lowercase, range(len(string.ascii_lowercase))))
    for letter in string.ascii_lowercase:
        shifted = mono_alphabetic_cipher._unshift_letter(letter)
        assert mono_alphabetic_cipher.keyspace[alphabet_lookup[shifted]] == letter
