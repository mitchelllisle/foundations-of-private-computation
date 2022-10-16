from privcomp import ShiftCipher, ShiftCipherAttack

if __name__ == '__main__':
    shift_cipher = ShiftCipher(shift=3)
    ciphertext = shift_cipher.encrypt('ax hello world')
    plaintext = shift_cipher.decrypt(ciphertext)

    shift_cipher_attack = ShiftCipherAttack(ciphertext)
    shift_cipher_attack.run()
