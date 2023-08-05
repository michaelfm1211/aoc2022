from collections import deque

# my implementation of part B, in retrospect, building off of 18a to solve 18b.
# flood fills from a boundary box

nodes = {}
for line in open('in'):
    pos = tuple(map(int, line.strip().split(',')))
    neighbors = []

    ds = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    for d in ds:
        new = (pos[0]+d[0], pos[1]+d[1], pos[2]+d[2])
        if new in nodes:
            neighbors.append(new)
            nodes[new].append(pos)
    nodes[pos] = neighbors

sa = 0
for n in nodes.values():
    sa += 6 - len(n)
print('Part A:', sa)

# flood fill with BFS to find exterior
bstart = (min(nodes, key=lambda x: x[0])[0]-1, min(nodes, key=lambda x: x[1])[1]-1,
          min(nodes, key=lambda x: x[2])[2]-1)
bend = (max(nodes, key=lambda x: x[0])[0]+1, max(nodes, key=lambda x: x[1])[1]+1,
        max(nodes, key=lambda x: x[2])[2]+1)
sa = 0
q = deque([bstart])
visited = set()
while q:
    pos = q.pop()
    if pos in visited:
        continue

    visited.add(pos)
    ds = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for dx, dy, dz in ds:
        new = (pos[0]+dx, pos[1]+dy, pos[2]+dz)
        if pos[0] < bstart[0] or pos[1] < bstart[1] or pos[2] < bstart[2]:
            continue
        elif pos[0] > bend[0] or pos[1] > bend[1] or pos[2] > bend[2]:
            continue

        if new in nodes:
            sa += 1
        else:
            q.append(new)
print('Part B:', sa)
