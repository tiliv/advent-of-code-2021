from collections import defaultdict
import itertools
import re
from typing import Iterator


Coord = int
HitMap = defaultdict[Coord, int]
Grid = defaultdict[Coord, HitMap]
Point = tuple[Coord, Coord]
Line = tuple[Point, Point]


RE_LINE = r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)'


def iter_lines() -> Iterator[str]:
    with open('input.txt') as f:
        yield from (line.strip() for line in f.readlines())


def get_lines() -> Iterator[Line]:
    for i, line in enumerate(iter_lines()):
        x1, y1, x2, y2 = map(int, re.match(RE_LINE, line).groupdict().values())
        if x1 == x2 or y1 == y2:
            # print(
            #     str(i + 1).rjust(3, ' '),
            #     f'({x1}, {y1}) -> ({x2}, {y2}) @',
            #     f'<x:{get_range(x1, x2)}>, y:{get_range(y1, y2)}>\n  ',
            #     list(walk_coords((x1, y1), (x2, y2))))
            yield (x1, y1), (x2, y2)


def walk_coords(a: Point, b: Point) -> Iterator[Point]:
    x1, y1 = a
    x2, y2 = b
    return itertools.zip_longest(
        get_range(x1, x2),
        get_range(y1, y2),
        fillvalue=x1 if x1 == x2 else y1)


def get_range(a: int, b: int) -> range:
    Δ: int = b - a
    sign: int = Δ // abs(Δ) if Δ else 1
    return range(a, b + sign, sign)


def write_grid(grid: Grid, lines: Iterator[Line]):
    for (x1, y1), (x2, y2) in lines:
        for x, y in walk_coords((x1, y1), (x2, y2)):
            grid[y][x] += 1


def dump(grid: Grid):
    y_values: list[int] = list(grid.keys())
    x_values: list[int] = list(itertools.chain.from_iterable(
        hits.keys()
        for hits in grid.values()
    ))
    for y in range(max(y_values) + 1):
        for x in range(max(x_values) + 1):
            print(
                # f'{x},{y}'.rjust(5, ' '),
                f'{grid[y][x] or "."}',
                end='')
        print()


if __name__ == '__main__':
    grid: Grid = defaultdict(lambda: defaultdict(int))
    write_grid(grid, get_lines())
    # dump(grid)
    answer: int = sum(
        sum(1 for v in x_lists.values() if v > 1)
        for x_lists in grid.values()
    )
    print(f'Answer: {answer}')
