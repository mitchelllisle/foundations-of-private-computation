from privcomp.ciphers.shift_cipher.cipher import ShiftCipher
from privcomp.logger import logger


class ShiftCipherAttack:
    def __init__(self, ciphertext: str):
        self.ciphertext: str = ciphertext
        self.attack_space: range = range(26)

    def run(self):
        for shift in self.attack_space:
            shift_cipher = ShiftCipher(shift)
            logger.info(shift_cipher.decrypt(self.ciphertext))
