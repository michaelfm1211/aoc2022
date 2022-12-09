import itertools
from operator import countOf

rows = [list(map(int, line.strip())) for line in open('in')]
cols = [[] for _ in range(len(rows))]
for row in rows:
    for i, el in enumerate(row):
        cols[i].append(el)

cnt = 0
for i, j in itertools.product(range(len(rows)), range(len(cols))):
    el = rows[i][j]

    xN = rows[i][:j+1]
    xP = rows[i][j:]
    yN = cols[j][:i+1]
    yP = cols[j][i:]

    vis = map(lambda lst: countOf(lst, el) == 1 and max(lst) == el,
              [xN, xP, yN, yP])
    if any(vis):
        cnt += 1
print(cnt)
