import re


def open_input():
    with open("input.txt") as f:
        f = f.readlines()  # 8 , 10
        towers = [i.rstrip("\n") for i in f[:8]]
        moves = [i.rstrip("\n") for i in f[10:]]
        return towers, moves


def get_cols(matrix: list):
    new_matrix = []
    for i in range(0, len(matrix[0]), 4):
        col = []
        for row in matrix:
            col.append(row[i : i + 4].strip())
        col.reverse()
        col = list(filter(lambda x: x != "", col))
        new_matrix.append(col)
    return new_matrix


def move_item(matrix, quantity, _from, _to):
    _from -= 1
    _to -= 1
    to_move = matrix[_from][-quantity:]
    matrix[_from] = matrix[_from][:-quantity]
    matrix[_to] = matrix[_to] + to_move


def main():
    towers, moves = open_input()
    moves = [re.findall("\d+", i) for i in moves]
    cols = get_cols(towers)
    cols = cols
    for i in moves:
        i = list(map(int, i))
        move_item(cols, *i)
    lasts = [i[-1] for i in cols]
    print("".join(lasts))
