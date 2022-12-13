import queue


def validNeighbors(grid, pt):
    height = ord(grid[pt[0]][pt[1]])
    valid = set()
    # x go up => right
    if pt[1]+1 < len(grid[pt[0]]) and ord(grid[pt[0]][pt[1]+1]) <= height + 1:
        valid.add((pt[0], pt[1] + 1))

    # y go up => down
    if pt[0] + 1 < len(grid) and ord(grid[pt[0] + 1][pt[1]]) <= height + 1:
        valid.add((pt[0] + 1, pt[1]))

    # x go down => left
    if pt[1] - 1 >= 0 and ord(grid[pt[0]][pt[1] - 1]) <= height + 1:
        valid.add((pt[0], pt[1] - 1))

    # y go down => up
    if pt[0] - 1 >= 0 and ord(grid[pt[0] - 1][pt[1]]) <= height + 1:
        valid.add((pt[0] - 1, pt[1]))

    return valid


def findLetter(grid, ch, rep):
    letter = None
    for x, row in enumerate(grid):
        if letter is not None:
            break
        for y, col in enumerate(row):
            if col == ch:
                letter = (x, y)
                grid[x][y] = rep
                break
    return letter


grid = [[*line.strip()] for line in open('in')]


# find start and end
s = findLetter(grid, 'S', 'a')
e = findLetter(grid, 'E', 'z')

# memoize neighbors
neighbors = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        neighbors[(i, j)] = validNeighbors(grid, (i, j))

# breadth first search
visited = set()
q = queue.Queue()
q.put((0, s))
while not q.empty():
    (cnt, pt) = q.get()
    if pt in visited:
        continue
    visited.add(pt)
    for neighbor in neighbors[pt]:
        if neighbor == e:
            print(cnt + 1)
            exit()
        q.put((cnt + 1, neighbor))
