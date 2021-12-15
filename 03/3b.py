from collections import Counter


def iter_lines():
    with open('input.txt') as f:
        yield from (line.strip() for line in f.readlines())


def parse_column(data: str) -> tuple[str, str]:
    counter = Counter(data)
    if len(set(counter.values())) < 2:  # same number of each
        return ['1', '0']  # use default config preference
    return [k for k, v in counter.most_common()]


def get_columns(lines: list[str]) -> Counter:
    """Write strings for each column of consecutive lines."""
    columns = Counter(dict.fromkeys(range(len(lines[0])), ''))
    for line in lines:
        columns.update(dict(enumerate(line)))
    return columns


def filter_lines(lines: list[str], column: int, value: str) -> tuple[list[str], str]:
    """
    Filter `lines` where `line[column]` equals the target bit value.
    """
    filtered = [line for line in lines if line[column] == value]
    if len(filtered) == 1:
        return filtered, filtered[0]
    return filtered, None


def decode(size=12) -> tuple[str, str]:
    lines: list[str] = list(iter_lines())
    columns: Counter = {k: v[::-1] for k, v in get_columns(lines).items()}

    o_lines: list[bool] = list(lines)
    co2_lines: list[bool] = list(lines)
    o_rating: str = None
    co2_rating: str = None
    for i in range(len(columns)):
        o_columns: Counter = {k: v[::-1] for k, v in get_columns(o_lines).items()}
        co2_columns: Counter = {k: v[::-1] for k, v in get_columns(co2_lines).items()}
        o_val = None
        co2_val = None

        if not o_rating:
            o_val, _ = parse_column(o_columns[i])
            o_lines, o_rating = filter_lines(o_lines, column=i, value=o_val)
            print(f'[{i}]   O {"_" * i}{o_val}{"_" * (size - i - 1)} ({len(o_lines)})')
            if o_rating:
                yield {'oxygen_efficiency_rating': o_rating}

        if not co2_rating:
            _, co2_val = parse_column(co2_columns[i])
            co2_lines, co2_rating = filter_lines(co2_lines, column=i, value=co2_val)
            print(f'[{i}] CO2 {"_" * i}{co2_val}{"_" * (size - i - 1)} ({len(co2_lines)})')
            if co2_rating:
                yield {'co2_scrubber_rating': co2_rating}


def extract_ratings() -> dict[str, str]:
    values = {}
    for rating in decode():
        values.update(rating)
    return values


if __name__ == '__main__':
    ratings = extract_ratings()
    answer: int = (
        int(ratings['oxygen_efficiency_rating'], base=2)
        * int(ratings['co2_scrubber_rating'], base=2)
    )
    print(f'Answer: {answer} ({ratings})')
