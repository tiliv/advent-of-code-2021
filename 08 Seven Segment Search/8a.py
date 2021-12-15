from typing import Iterator


Pattern = list[str]
Output = list[str]

UNIQUE_SIGNALS = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}


def iter_patterns() -> Iterator[tuple[Pattern, Output]]:
    with open('input.txt') as f:
        for line in f.readlines():
            patterns, output = line.split(' | ')
            yield patterns.split(), output.split()


if __name__ == '__main__':
    appearances = 0
    for patterns, output in iter_patterns():
        unique_signals = list(filter(
            lambda s: len(s) in UNIQUE_SIGNALS, output))
        appearances += len(unique_signals)
        # print(f'{len(unique_signals)} {unique_signals=} {output=}')
    answer = appearances
    print(f'Answer: {answer}')
