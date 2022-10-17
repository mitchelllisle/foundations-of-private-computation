from privcomp.ciphers.cipher import AbstractCipher


def test_clean_text():
    text = 'This is a test.'
    cleaned = AbstractCipher.clean_text(text)

    assert cleaned == 'this is a test'
