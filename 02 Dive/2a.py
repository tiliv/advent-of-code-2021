import enum


class Direction(enum.Enum):
    FORWARD = 'forward'
    UP = 'up'
    DOWN = 'down'


Location = dict[str, int]
Vector = tuple[Direction, int]


def iter_lines():
    with open('input.txt') as f:
        yield from map(transform_line, f.readlines())


def transform_line(line: str) -> Vector:
    direction, value = line.split()
    return Direction(direction), int(value)


def move(direction: Direction, size: int = 1, *, x: int, y: int) -> Location:
    return {
        'x': x + size * int(direction == Direction.FORWARD),
        'y': (y + size * int(direction == Direction.DOWN)
                - size * int(direction == Direction.UP)),
    }


if __name__ == '__main__':
    direction: Direction
    value: int

    location: Location = {'x': 0, 'y': 0}
    for direction, value in iter_lines():
        # input(f'{direction.value} {value} ({location!r}) ')
        location = move(direction, size=value, **location)

    answer = location['x'] * location['y']
    print(f'Answer: {answer!r} ({location!r})')
