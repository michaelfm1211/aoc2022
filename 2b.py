trans = {'A': 0, 'B': 1, 'C': 2}
res = {'X': 0, 'Y': 3, 'Z': 6}


def move(a, res):
    if res == 'Y':  # tie
        return trans[a] + 1
    if res == 'Z':  # win
        return ((trans[a] + 1) % 3) + 1
    # loose
    keys = list(trans.keys())
    return trans[keys[keys.index(a) - 1]] + 1


print(move('A', 'X'))  # should be 3

total = 0
with open('input.txt') as f:
    for line in f.readlines():
        total += res[line[2]] + move(line[0], line[2])
print(total)
