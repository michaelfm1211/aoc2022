from itertools import pairwise


def ptsBetween(p1, p2):
    if p1[0] == p2[0]:
        smaller = min(p1[1], p2[1])
        for y in range(abs(p1[1] - p2[1]) + 1):
            yield [p1[0], smaller+y]
    else:
        smaller = min(p1[0], p2[0])
        for x in range(abs(p1[0] - p2[0]) + 1):
            yield [smaller + x, p1[1]]


block = set()
for line in open('in'):
    endpts = [list(map(int, pt.strip().split(','))) for pt in line.split('->')]
    for (p1, p2) in pairwise(endpts):
        for pt in ptsBetween(p1, p2):
            block.add(tuple(pt))

maxY = max(map(lambda pt: pt[1], block))

cnt = 0
sand = (500, 0)
while sand[1] <= maxY:
    if (sand[0], sand[1]+1) not in block:
        sand = (sand[0], sand[1] + 1)
    elif (sand[0]-1, sand[1]+1) not in block:
        sand = (sand[0]-1, sand[1] + 1)
    elif (sand[0]+1, sand[1]+1) not in block:
        sand = (sand[0]+1, sand[1] + 1)
    else:
        cnt += 1
        block.add(sand)
        sand = (500, 0)

print(cnt)
