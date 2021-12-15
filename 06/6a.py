def get_ages() -> list[int]:
    with open('input.txt') as f:
        line, = f.readlines()
    return list(map(int, line.split(',')))


def step_day(ages: list[int]):
    for i, age in enumerate(ages[:]):
        age, *newborn = tick(age)
        ages[i] = age
        ages.extend(newborn)


def tick(age: int) -> list[int]:
    if not age:
        return [6, 8]
    return [age - 1]


if __name__ == '__main__':
    ages: list[int] = get_ages()
    for day in range(18):
        step_day(ages)
    answer = len(ages)
    print(f'Answer: {answer}')
