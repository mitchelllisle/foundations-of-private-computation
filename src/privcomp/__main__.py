from privcomp.ciphers.shift_cipher.shift import ShiftCipher

if __name__ == '__main__':
    ciphter = ShiftCipher()
    ciphertext = ciphter.encrypt('hello world')
    plaintext = ciphter.decrypt(ciphertext)
    pass
