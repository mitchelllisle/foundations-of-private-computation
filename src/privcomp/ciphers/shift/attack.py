from typing import List

from privcomp.ciphers.shift.cipher import ShiftCipher


class ShiftCipherAttack:
    def __init__(self, ciphertext: str):
        self.ciphertext: str = ciphertext
        self.attack_space: range = range(26)

    def run(self) -> List[str]:
        plaintexts = []
        for shift in self.attack_space:
            shift_cipher = ShiftCipher(shift)
            plaintexts.append(shift_cipher.decrypt(self.ciphertext))
        return plaintexts
