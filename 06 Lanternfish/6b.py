from collections import Counter


def get_ages() -> Counter:
    with open('input.txt') as f:
        line, = f.readlines()
    ages = map(int, line.split(','))
    return Counter(ages)


def shift(ages: Counter, newborn_age: int, reset_age: int) -> Counter:
    ready: int = ages.get(0, 0)
    new_ages = Counter({
        age - 1: quantity
        for age, quantity in ages.items()
        if age
    })
    return new_ages + Counter({
        newborn_age: ready,
        reset_age: ready,
    })


if __name__ == '__main__':
    ages: Counter = get_ages()
    for day in range(256):
        ages = shift(ages, newborn_age=8, reset_age=6)
    answer = sum(ages.values())
    print(f'Answer: {answer}')
