from string import ascii_letters


def open_input():
    with open("input.txt") as f:
        _input = f.readlines()
        _input = [i.strip() for i in _input]
    return _input


def main():
    row_vals = []
    rucksack = open_input()
    rucksack = [
        list(set(a[: len(a) // 2]).intersection(set(a[len(a) // 2 :])))[0]
        for a in rucksack
    ]
    for idx in rucksack:
        row_vals.append(ascii_letters.index(idx) + 1)
    total_sum = sum(row_vals)
    # second part
    row_vals = []
    rucksack = open_input()
    temp = [
        ascii_letters.index(
            list(set(rucksack[i]).intersection(rucksack[i + 1], rucksack[i + 2]))[0]
        )
        + 1
        for i in range(0, len(rucksack), 3)
    ]

    print(total_sum)
    print(sum(temp))
