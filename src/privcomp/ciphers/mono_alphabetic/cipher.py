import string

from pipe import map

from privcomp.ciphers.cipher import AbstractCipher


class MonoAlphabeticCipher(AbstractCipher):
    """Mono Alphabetic cipher
    We've seen that the shift cipher is easy to break as the number of possible keys was just 26. A better approach
    would be to simply substitute each letter of the alphabet by another random letter. This way we would have 26!
    different permutations (that is a number of the order of ). Here we cannot do exhaustive search, it would take so
    long for our computer. A secret key could be for instance "bdeoinmkclxuqzytpwvjgafrsh", where the ciphertext for
    "a" is "b", the ciphertext for "b" is "d" and so on.
    """

    def __init__(self, secret_key: str = 'xtkcndbjipyvmfeslagourwqhz'):
        self.secret_key = secret_key
        self._secret_key_lookup = dict(zip(self.secret_key, range(len(self.secret_key))))

    @classmethod
    def generate(cls) -> str:
        keyspace = list(string.ascii_lowercase)
        cls.random.shuffle(keyspace)
        return ''.join(keyspace)

    def _letter_validation(self, letter: str) -> str:
        if letter.lower() not in f'{self.secret_key} ':
            raise ValueError(f'letter can only be 1 character length and must be in alphabet. Problem letter: {letter}')
        return letter.lower()

    def _shift_letter(self, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            letter_idx = ord(letter.lower()) - 97
            return self.secret_key[letter_idx]
        return letter

    def _unshift_letter(self, letter: str) -> str:
        letter = self._letter_validation(letter)
        if letter != ' ':
            return self.keyspace[self._secret_key_lookup[letter]]
        return letter

    def encrypt(self, plaintext: str) -> str:
        ciphertext = list(plaintext.lower().strip().replace('\n', '') | map(self._shift_letter))
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = list(ciphertext.lower().strip().replace('\n', '') | map(self._unshift_letter))
        return ''.join(plaintext)
