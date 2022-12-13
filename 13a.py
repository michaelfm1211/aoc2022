from ast import literal_eval


def check(p1, p2):
    if p1 == p2:
        return None

    if type(p1) == int and type(p2) == int:
        return p1 < p2
    elif type(p1) == list and type(p2) == list:
        for i in range(max(len(p1), len(p2))):
            try:
                res = check(p1[i], p2[i])
            except IndexError:
                return len(p1) < len(p2)

            if res is not None:
                return res
    elif type(p1) == int:
        return check([p1], p2)
    elif type(p2) == int:
        return check(p1, [p2])
    print('????')


data = open('in').read()
pairs = [pair.strip().split('\n') for pair in data.split('\n\n')]

s = 0
for i, pair in enumerate(pairs):
    lines = [literal_eval(line) for line in pair]
    if check(lines[0], lines[1]):
        s += i + 1
print(s)
