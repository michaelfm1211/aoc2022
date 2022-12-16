#
#
#   RUN WITH PYPY, NOT CPYTHON.
#
#   otherwise, it won't run fast enough.
#   other methods are probably faster, but this an extension of my part A
#
#   merge() function could probably be optimized by not using list.sort()
#
#

import re


def limit(val, low, high):
    if val < low:
        return low
    elif val > high:
        return high
    return val


def merge(lst):
    lst.sort()
    new = [lst[0]]
    for r in lst[1:]:
        if r[1] < new[-1][1]:
            continue
        elif r[0] <= new[-1][1] + 1:
            new[-1][1] = r[1]
        else:
            new.append(r)
    return new


sensors = []
for line in open('in'):
    n = list(map(int, re.findall('-?[0-9]+', line)))
    dist = abs(n[0] - n[2]) + abs(n[1] - n[3])
    sensors.append(((n[0], n[1]), dist))

# find intervals
# M = 20
M = 4000000
lines = []
for y in range(M):
    print('       ', y+1, '/', M, end='\r')
    lines.append([])
    for sensor in sensors:
        [pos, dist] = sensor
        if pos[1] + dist >= y and pos[1] - dist <= y:
            width = (2*dist+1) - 2*abs(y-pos[1])
            start = limit(pos[0]-width//2, 0, M)
            end = limit(pos[0]+width//2, 0, M)
            lines[-1].append([start, end])
    lines[-1] = merge(lines[-1])

# find gap
print()
for i, line in enumerate(lines):
    if line != [[0, M]]:
        print('=====================')
        x = line[0][1] + 1
        print('\nx=', x, 'y=', i)
        print('Tuning frequency:', x*4000000 + i)
        break
