def iter_lines():
    with open('input.txt') as f:
        yield from (int(line) for line in f.readlines())


def iter_diffs(size=3):
    prior = 0
    values = list(iter_lines())
    for i in range(len(values)):
        window = values[i:i + size]
        if None in window:
            break
        value = sum(window)
        if i > 0:
            yield value - prior
        prior = value


if __name__ == '__main__':
    answer = len([
        diff
        for diff in iter_diffs()
        if diff > 0
    ])
    print(f'Answer: {answer!r}')
