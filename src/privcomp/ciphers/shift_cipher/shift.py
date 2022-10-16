import string

from pipe import map


class ShiftCipher:
    """Shift Cipher
    One of the oldest known ciphers is the Shift cipher. In this cipher we encrypt the alphabet by shifting a certain
    number of places the letters of our message. Julius Caesar used the Shift cipher to communicate secretly with his
    military, but he used a fixed shift of three, this is why the Shift cipher with the specific shift of three is known
    as the Caesar's cipher but is nothing less that a particular case for the shift cipher.

    In the shift cipher the two interlocutors (the sender and the receiver) have to agree on a common secret key, this
    is, the shift or a number in between 0 and 26 (corresponding to the 26 letters in the english alphabet). They have
    to meet in person to agree on which secret key they are going to use so that they are sure nobody else knows the
    key.

    The shift cipher is a substitution cipher meaning that each character of our message is substituted by another
    character, let's see the substitution for the secret_key "b", i.e. a shift of 1
    """

    def __init__(self, shift: int = 3):
        self.shift = shift
        self.alphabet: str = string.ascii_lowercase
        self._shifted_alphabet: str = self._shift_alphabet()

    def _shift_alphabet(self):
        return self.alphabet[self.shift :] + self.alphabet[: self.shift]

    def _shift_letter(self, letter: str) -> str:
        if letter.lower() not in f'{self.alphabet} ':
            raise ValueError('letter can only be 1 character length and must be in alphabet')

        if letter != ' ':
            letter_idx = ord(letter.lower()) - 97
            return self._shifted_alphabet[letter_idx]
        return letter

    def _unshift_letter(self, letter: str) -> str:
        if letter != ' ':
            letter_idx = ord(letter.lower()) - 97 - 3
            return self.alphabet[letter_idx]
        return letter

    def encrypt(self, plaintext: str) -> str:
        ciphertext = list(plaintext | map(self._shift_letter))
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = list(ciphertext | map(lambda letter: self._unshift_letter(letter)))
        return ''.join(plaintext)
