from collections import Counter


def iter_lines():
    with open('input.txt') as f:
        yield from (line.strip() for line in f.readlines())


def decode(size=12) -> tuple[str, str]:
    columns = Counter(dict.fromkeys(range(size), ''))
    for line in iter_lines():
        columns.update(dict(enumerate(line)))

    column: str
    gamma_rate = ''
    epsilon_rate = ''
    for column in columns.values():
        g, e = [k for k, v in Counter(column).most_common()]
        gamma_rate += g
        epsilon_rate += e

    return gamma_rate, epsilon_rate


if __name__ == '__main__':
    gamma_rate, epsilon_rate = decode()
    answer: int = int(gamma_rate, base=2) * int(epsilon_rate, base=2)
    print(f'Answer: {answer}')
