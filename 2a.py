u1 = {'A': 1, 'B': 2, 'C': 3}
u2 = {'X': 1, 'Y': 2, 'Z': 3}


def result(a, b):
    if u1[a] == u2[b]:
        return 3
    if (a == 'A' and b == 'Y') or (a == 'B' and b == 'Z') or (a == 'C' and b == 'X'):
        return 6
    return 0


total = 0
with open('input.txt') as f:
    for line in f.readlines():
        score = u2[line[2]] + result(line[0], line[2])
        total += score
print(total)
