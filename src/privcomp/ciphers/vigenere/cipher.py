from typing import Set

from privcomp.ciphers.cipher import AbstractCipher
from privcomp.text_utils import starmap


class VigenereCipher(AbstractCipher):
    def __init__(self, key: str = 'jsf'):
        self.key = key
        self.key_length = len(self.key)

    def _shift_letter(self, shift_by: int, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            idx = ord(letter) - 97
            shift_idx = ord(self.key[shift_by % self.key_length]) - 97
            return self.keyspace[(idx + shift_idx) % self.keyspace_size]
        return letter

    def _unshift_letter(self, shift_by: int, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            idx = ord(letter) - 97
            shift_idx = ord(self.key[shift_by % self.key_length]) - 97
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
