import string
from random import SystemRandom

from pipe import map


class MonoAlphabeticCipher:

    random = SystemRandom()

    def __init__(self, keyspace: str = 'xtkcndbjipyvmfeslagourwqhz'):
        self.keyspace = keyspace
        self._keyspace_lookup = dict(zip(self.keyspace, range(len(self.keyspace))))
        self.alphabet = string.ascii_lowercase

    @classmethod
    def generate(cls) -> str:
        keyspace = list(string.ascii_lowercase)
        cls.random.shuffle(keyspace)
        return ''.join(keyspace)

    def _letter_validation(self, letter: str) -> str:
        if letter.lower() not in f'{self.keyspace} ':
            raise ValueError(f'letter can only be 1 character length and must be in alphabet. Problem letter: {letter}')
        return letter.lower()

    def _shift_letter(self, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            letter_idx = ord(letter.lower()) - 97
            return self.keyspace[letter_idx]
        return letter

    def _unshift_letter(self, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            return self.alphabet[self._keyspace_lookup[letter]]
        return letter

    def encrypt(self, plaintext: str) -> str:
        ciphertext = list(plaintext.lower().strip().replace('\n', '') | map(self._shift_letter))
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = list(ciphertext.lower().strip().replace('\n', '') | map(self._unshift_letter))
        return ''.join(plaintext)
