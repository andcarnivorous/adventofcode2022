with open("input1.txt") as f:
    var = f.read()


def strip(stringa):
    return stringa.strip("\n ")


def get_sums(values):
    values = map(strip, var.split("\n\n"))
    values = [sum(map(int, val.split("\n"))) for val in values]
    return values


def get_best_elf(values):
    values = get_sums(values)
    return max(values)


def get_top_three(values):
    values = get_sums(values)
    return sorted(values, reverse=True)[:3]


print(get_best_elf(var))
print(sum(get_top_three(var)))
