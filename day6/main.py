from collections import deque


def check_repetitions(_input, n):
    dump = []
    tmp = deque()
    for i in _input:
        tmp.append(i)
        if len(set(tmp)) == n:
            return "".join(tmp), dump
        elif len(tmp) == n:
            dump.append(tmp.popleft())


def main():
    with open("input.txt") as f:
        f = f.read()
    n = 14
    series, dump = check_repetitions(f, n)
    print(series, len(dump) + n)
