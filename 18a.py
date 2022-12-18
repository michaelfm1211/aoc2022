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
print(sa)
