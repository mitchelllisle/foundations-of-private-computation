from typing import List

from privcomp.ciphers.vigenere.cipher import VigenereCipher


class OneTimePad(VigenereCipher):
    @classmethod
    def sample(cls, text: str, size: int) -> str:
        return ' '.join(cls.random.sample(text.split(), size))

    @classmethod
    def generate(cls, size: int = 3) -> str:
        keys: List[str] = []
        while len(keys) < size:
            keys.append(cls.keyspace[cls.random.randrange(cls.keyspace_size)])
        return ''.join(keys)
