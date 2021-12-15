def get_positions() -> list[int]:
    with open('input.txt') as f:
        line, = f.readlines()
    return list(map(int, line.split(',')))


def calc_fuel(position: int, positions: list[int]) -> int:
    return sum([
        abs(position - crab)
        for crab in positions
    ])


if __name__ == '__main__':
    positions: list[int] = get_positions()
    fuel, position = min(
        (calc_fuel(i, positions), i)
        for i in range(len(positions)))
    print(f'Answer: {position}: {fuel}')
