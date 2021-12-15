from dataclasses import dataclass, field


Match = set[int]
BOARD_SIZE = 5
BOARD_RANGE = range(BOARD_SIZE)


@dataclass
class Board:
    lines: list[int]
    numbers: set[int] = field(default_factory=set)
    diags: list[Match] = field(
        default_factory=lambda: [set(), set()])
    cols: list[Match] = field(
        default_factory=lambda: [set() for i in BOARD_RANGE])
    rows: list[Match] = field(
        default_factory=lambda: [set() for i in BOARD_RANGE])

    def __post_init__(self):
        for row, line in enumerate(self.lines):
            self.rows[row] = set(line)
            for col, num in enumerate(line):
                self.numbers.add(num)
                self.cols[col] = set([line[col] for line in self.lines])
                if row == col:
                    self.diags[0].add(num)
                if row + col == BOARD_SIZE - 1:
                    self.diags[1].add(num)

    def score(self, numbers: list[int]):
        # print('-', sum(self.numbers - set(numbers)))
        return sum(self.numbers - set(numbers)) * numbers[-1]

    def check(self, numbers: list[int]):
        self._numbers = set(numbers)
        return any([
            # list(filter(lambda match: self._numbers & match == match, self.diags)),
            list(filter(lambda match: self._numbers & match == match, self.cols)),
            list(filter(lambda match: self._numbers & match == match, self.rows)),
        ])

    def __repr__(self):
        return '\n'.join(map(
            lambda line: ''.join([
                f' {"*" if num in self._numbers else " "}{str(num).rjust(2, " ")}'
                for num in line
            ]),
            self.lines))


def read() -> tuple[list[int], list[Board]]:
    boards: list[Board] = []
    with open('input.txt') as f:
        numbers, *lines = map(str.strip, f.readlines())
        i = 1
        while lines[i:]:
            if not lines[i]:
                i += 1
                continue
            boards.append(
                Board(lines=list(map(
                    lambda line: list(map(int, line.split())),
                    lines[i:i+5]))))
            i += 5
    return list(map(int, numbers.split(','))), boards


if __name__ == '__main__':
    numbers, boards = read()
    _boards = {id(board): board for board in boards}
    winners: dict[int, Board] = {}
    i = 0
    while not winners and i < len(numbers):
        i += 1
        called = numbers[:i]
        winners = {
            id(board): board.score(called)
            for board in boards
            if board.check(called)
        }
        print(f'Round {len(called)} [{called[-1]}]: {len(winners)} / {len(boards)}')
        if len(winners) + 1 >= len(boards):
            winners = {
                _id: winners[_id]
                for _id in set(_boards) - set(winners.values())
            }
            break
        else:
            winners = {}

    for winner, score in dict(sorted(winners.items())).items():
        board = _boards[winner]
        print(f'#{boards.index(board)}: {score}')
        # print(winner)
