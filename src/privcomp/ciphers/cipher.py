import re
import string
from abc import ABC, abstractmethod
from random import SystemRandom

from privcomp.types import CipherText, PlainText


class AbstractCipher(ABC):
    random: SystemRandom = SystemRandom()
    keyspace: str = string.ascii_lowercase
    keyspace_size: int = len(keyspace)

    def _letter_validation(self, letter: str) -> str:
        if letter.lower() not in f'{self.keyspace} ':
            raise ValueError(f'letter can only be 1 character length and must be in alphabet. Problem letter: {letter}')
        return letter.lower()

    @staticmethod
    def clean_text(text: str) -> str:
        text = text.lower().replace('\n', '').strip()
        text = re.sub(rf'[{string.punctuation}]', '', text)
        text = re.sub(r'\d', '', text)
        text = re.sub(r'\s{2,}', ' ', text)
        return text

    @abstractmethod
    def encrypt(self, plaintext: PlainText) -> CipherText:
        pass

    @abstractmethod
    def decrypt(self, ciphertext: CipherText) -> PlainText:
        pass
