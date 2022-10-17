from typing import Set

from privcomp.ciphers.cipher import AbstractCipher
from privcomp.text_utils import letter_to_int, starmap


class VigenereCipher(AbstractCipher):
    """Vigenère Cipher
    Let's go for an even more difficult cipher to crack, the Vigenère cipher.
    The first difficulty of the Vigenere cipher is that the length of the key is arbitrary and indicates the permutation
    of the text.
    Our plaintext is `ddddd` and we encrypt it using the key  of length 3. It is easy to see how it works. The first
    letter of the plaintext is shifted  (shift of 0), the second shifted  (shift of 1 position) and the third one by
    (shift of 3 positions).

    We've chosen as key a random chain of size 3, this is esz. Again, e is shifted (4 positions), r shifted
    (9 positions) and  shifted by  (7 positions). Then, the next character  is shifted by the first letter of the key,
    this results.
    """

    def __init__(self, key: str = 'jsf'):
        self.key = key
        self.key_length = len(self.key)

    def _shift_letter(self, shift_by: int, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            idx = letter_to_int(letter)
            shift_idx = letter_to_int(self.key[shift_by % self.key_length])
            return self.keyspace[(idx + shift_idx) % self.keyspace_size]
        return letter

    def _unshift_letter(self, shift_by: int, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            idx = letter_to_int(letter)
            shift_idx = letter_to_int(self.key[shift_by % self.key_length])
            return self.keyspace[(idx - shift_idx) % self.keyspace_size]
        return letter

    def encrypt(self, plaintext: str) -> str:
        cleaned = self.clean_text(plaintext)
        ciphertext = list(enumerate(cleaned) | starmap(self._shift_letter))
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        ciphertext = list(enumerate(ciphertext) | starmap(self._unshift_letter))  # type: ignore
        return ''.join(ciphertext)

    @classmethod
    def generate(cls, size: int = 3) -> str:
        if size > cls.keyspace_size:
            raise ValueError(f'max size allowed is {cls.keyspace_size}, size {size} is too large.')
        keys: Set[str] = set()
        while len(keys) < size:
            keys.add(cls.keyspace[cls.random.randrange(cls.keyspace_size)])
        return ''.join(keys)
