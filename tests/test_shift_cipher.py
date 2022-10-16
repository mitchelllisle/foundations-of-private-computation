import string


def test_shift_cipher(shift_cipher):
    assert len(shift_cipher.keyspace) == 26


def test_shift_cipher_default_shift(shift_cipher):
    assert shift_cipher.shift == 3


def test_encrypt(shift_cipher, shift_cipher_plaintext):
    encrypted = shift_cipher.encrypt(shift_cipher_plaintext)
    assert encrypted != shift_cipher_plaintext


def test_decrypt(shift_cipher, shift_cipher_plaintext, shift_cipher_text):
    decrypted = shift_cipher.decrypt(shift_cipher_text)
    assert shift_cipher_plaintext.strip().replace('\n', '') == decrypted


def test_shift_letter(shift_cipher):
    for idx, letter in enumerate(string.ascii_lowercase):
        shifted = shift_cipher._shift_letter(letter)
        assert shifted == shift_cipher._shifted_keyspace[idx]
        assert shift_cipher.keyspace[idx] == letter


def test_unshift_letter(shift_cipher):
    for letter in string.ascii_lowercase:
        shifted = shift_cipher._unshift_letter(letter)
        letter_idx = ord(shifted.lower()) - 97
        assert shifted == shift_cipher.keyspace[letter_idx]


def test_attack_works(shift_cipher_attack, shift_cipher_plaintext):
    output = shift_cipher_attack.run()
    assert len(output) == 26
    assert output[3] == shift_cipher_plaintext
