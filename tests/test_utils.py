import string

import pytest

from privcomp.ciphers.cipher import AbstractCipher
from privcomp.text_utils import letter_count, letter_to_int


def test_clean_text():
    text = 'This is a test.'
    cleaned = AbstractCipher.clean_text(text)

    assert cleaned == 'this is a test'


@pytest.mark.parametrize(
    'case', [(string.ascii_lowercase, [1 for _ in string.ascii_lowercase]), ('abbcccdddd', [4, 3, 2, 1])]
)
def test_letter_count(case):
    count = letter_count(case[0])
    assert [x[1] for x in count] == case[1]


def test_letter_to_int():
    for index, letter in enumerate(string.ascii_lowercase):
        assert letter_to_int(letter) == index
