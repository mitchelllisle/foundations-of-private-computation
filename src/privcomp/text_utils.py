from typing import List, Tuple

from pipe import Pipe, filter, groupby, map, sort


@Pipe
def starmap(iterable, selector):
    for element in iterable:
        yield selector(*element)


def letter_count(text: str) -> List[Tuple[str, int]]:
    return list(
        text
        | filter(lambda val: val != ' ')
        | groupby(lambda val: val)
        | map(lambda group: (group[0], len(list(group[1]))))
        | sort(lambda group: group[1], reverse=True)
    )


def letter_to_int(letter: str) -> int:
    return ord(letter) - 97
