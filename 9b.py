def sgn(n):
    return 1 if n > 0 else -1


def touching(h, t):
    diff = (abs(h[0]-t[0]), abs(h[1]-t[1]))
    return diff == (0, 0) or diff == (1, 0) or diff == (0, 1) or diff == (1, 1)


def updateHead(h, cmd):
    if cmd[0] == 'R':
        h[0] += 1
    elif cmd[0] == 'L':
        h[0] -= 1
    elif cmd[0] == 'U':
        h[1] += 1
    elif cmd[0] == 'D':
        h[1] -= 1


def updateTail(t, h):
    d = (h[0]-t[0], h[1]-t[1])
    ad = (abs(d[0]), abs(d[1]))
    if ad == (0, 0) or ad == (1, 0) or ad == (0, 1) or ad == (1, 1):
        # touching, => no movement
        pass
    elif ad == (2, 0) or ad == (0, 2):
        # on same row/col, => move 1
        axis = ad.index(2)
        t[axis] += sgn(d[axis])
    else:
        # must move on a diagnol
        t[0] += sgn(d[0])
        t[1] += sgn(d[1])


tLocs = {(0, 0)}
rope = [[0, 0] for _ in range(9)]
h = [0, 0]

for line in open('in'):
    cmd = line.strip().split(' ')
    for i in range(int(cmd[1])):
        updateHead(h, cmd)

        # treat each node as a tail/head
        last = h
        for t in rope:
            updateTail(t, last)
            last = t

        print(rope[-1])
        tLocs.add(tuple(rope[-1]))

print(len(tLocs))
