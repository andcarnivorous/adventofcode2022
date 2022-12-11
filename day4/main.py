def rangify(start, end):
    return set(map(str, list(range(start, end + 1))))


def split_start_end(dashed_pair):
    split_ranges = list(map(int, dashed_pair.split("-")))
    return rangify(*split_ranges)


def open_input():
    with open("input.txt") as f:
        _input = f.readlines()
        _input = [i.strip() for i in _input]
    return _input


def main():
    assignment_pairs = open_input()
    assignment_pairs = [pair.split(",") for pair in assignment_pairs]
    full_match = 0
    inter_match = 0
    for pair_a, pair_b in assignment_pairs:
        range_a = split_start_end(pair_a)
        range_b = split_start_end(pair_b)
        subset_a = range_a.issubset(range_b)
        subset_b = range_b.issubset(range_a)
        if subset_a or subset_b:
            full_match += 1
        inter_a = range_a.intersection(range_b)
        if inter_a:
            inter_match += 1
    # first part
    print(full_match)
    # second part
    print(inter_match)
