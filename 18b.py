from itertools import product
from collections import queue


# get all air blocks
blocks = [tuple(map(int, line.strip().split(','))) for line in open('in')]
airs = set()
for x, y, z in blocks:
    ds = product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))
    for dx, dy, dz in ds:
        if dx == dy == dz == 0:
            continue

        new = (x+dx, y+dy, z+dz)
        if new not in blocks:
            airs.add(new)
# get an outermost air
outermost = max(airs)

# connect all the air blocks
graph = {}
for pos in airs:
    neighbors = []
    ds = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for dx, dy, dz in ds:
        new = (pos[0]+dx, pos[1]+dy, pos[2]+dz)
        if new in graph:
            neighbors.append(new)
            graph[new].append(pos)
    graph[pos] = neighbors

# get disconnected groups with DFS
groups = []
unvisited = set(graph)
while len(unvisited) > 0:
    groups.append([])
    start = next(iter(unvisited))

    q = queue([start])
    while q:
        v = q.pop()
        if v in unvisited:
            unvisited.remove(v)
            groups[-1].append(v)
            for n in graph[v]:
                q.append(n)

# calc surface area of outermost group
for group in groups:
    if outermost not in group:
        continue

    sa = 0
    for x, y, z in group:
        ds = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
              (0, 0, -1)]
        for dx, dy, dz in ds:
            if (x+dx, y+dy, z+dz) in blocks:
                sa += 1
    print(sa)
