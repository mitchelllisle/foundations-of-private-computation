import string
from typing import List, Tuple

from pipe import filter, groupby, map, sort


def clean_text(text: str) -> str:
    words = text.split()
    processed = list(
        words | filter(lambda word: all([True if letter in string.ascii_lowercase else False for letter in word]))
    )
    return ' '.join(processed)


def letter_count(text: str) -> List[Tuple[str, int]]:
    return list(
        text
        | filter(lambda val: val != ' ')
        | groupby(lambda val: val)
        | map(lambda group: (group[0], len(list(group[1]))))
        | sort(lambda group: group[1], reverse=True)
    )
