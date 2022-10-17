import string
from typing import Dict, Tuple

from privcomp.ciphers.mono_alphabetic.cipher import MonoAlphabeticCipher
from privcomp.text_utils import letter_count


class MonoAlphabeticCipherAttack:
    def __init__(self):
        self.mc = MonoAlphabeticCipher('tizmxsarjchdlpgqwenbykvofu')
        self.keyspace = string.ascii_lowercase
        self.letter_frequency = [
            ('a', 0.082),
            ('b', 0.015),
            ('c', 0.028),
            ('d', 0.043),
            ('e', 0.13),
            ('f', 0.022),
            ('g', 0.02),
            ('h', 0.061),
            ('i', 0.07),
            ('j', 0.0015),
            ('k', 0.0077),
            ('l', 0.04),
            ('m', 0.024),
            ('n', 0.067),
            ('o', 0.075),
            ('p', 0.019),
            ('q', 0.00095),
            ('r', 0.06),
            ('s', 0.063),
            ('t', 0.091),
            ('u', 0.028),
            ('v', 0.0098),
            ('w', 0.024),
            ('x', 0.0015),
            ('y', 0.002),
            ('z', 0.00074),
        ]
        # sorting is important for comparison to derived keyspace
        self.letter_frequency.sort(key=lambda x: x[1], reverse=True)

    def calculate_accuracy(self, derived_keyspace: str) -> float:
        correct, incorrect = 0, 0
        for real, derived in zip(self.mc.secret_key, derived_keyspace):
            if real == derived:
                correct += 1
            else:
                incorrect += 1
        return correct / (correct + incorrect)

    def run(self, plaintext: str) -> Tuple[str, float]:
        encrypted = self.mc.encrypt(plaintext)

        lc = letter_count(encrypted)
        key_dict: Dict[str, str] = {}
        for (english_letter, _), (ctx_letter, _) in zip(self.letter_frequency, lc):
            if key_dict.get(english_letter) is None:
                key_dict[english_letter] = ctx_letter

        derived_keyspace = ''.join(
            [key_dict[letter] if key_dict.get(letter) is not None else '_' for letter in self.keyspace]
        )

        hacked_mc = MonoAlphabeticCipher(derived_keyspace)
        decrypted = hacked_mc.decrypt(encrypted)

        accuracy = self.calculate_accuracy(derived_keyspace)
        return decrypted, accuracy
