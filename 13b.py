from ast import literal_eval
from functools import cmp_to_key


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


def cmp(p1, p2):
    res = check(p1, p2)
    if res is None:
        return 0
    elif res is True:
        return -1
    elif res is False:
        return 1


packets = filter(lambda s: len(s) > 0, [line.strip() for line in open('in')])
packets = [literal_eval(s) for s in packets]
packets.extend([[[2]], [[6]]])
packets.sort(key=cmp_to_key(cmp))

d = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
print(d)
