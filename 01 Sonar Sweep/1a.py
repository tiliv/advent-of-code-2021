def iter_lines():
    with open('input.txt') as f:
        yield from (int(line) for line in f.readlines())


def iter_diffs():
    prior = 0
    for i, depth in enumerate(iter_lines()):
        if i > 0:
            yield depth - prior
        prior = depth


if __name__ == '__main__':
    answer = len([
        diff
        for diff in iter_diffs()
        if diff > 0
    ])
    print(f'Answer: {answer!r}')
