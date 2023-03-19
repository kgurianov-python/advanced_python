from enum import Enum
from typing import Iterator


class Mode(Enum):
    ODD = 1
    EVEN = 2


def the_generator(bound: int) -> Iterator[int]:
    for i in range(bound):
        yield i


def the_odd_even_gen(mode: Mode, bound: int) -> Iterator[int]:
    for i in range(mode.value, bound, 2):
        yield i


if __name__ == '__main__':
    print(*the_generator(10))
    print(*the_odd_even_gen(Mode.EVEN, 10))
    print(*the_odd_even_gen(Mode.ODD, 10))
