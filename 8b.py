import itertools

rows = [list(map(int, line.strip())) for line in open('in')]
cols = [[] for _ in range(len(rows))]
for row in rows:
    for i, el in enumerate(row):
        cols[i].append(el)

scenic = []
for i, j in itertools.product(range(len(rows)), range(len(cols))):
    el = rows[i][j]

    dirs = [rows[i][:j][::-1], rows[i][j+1:], cols[j][:i][::-1], cols[j][i+1:]]
    score = 1
    for direc in dirs:
        inview = list(itertools.takewhile(lambda x: el > x, direc))
        score *= len(inview)+1 if inview != direc else len(inview)
    scenic.append(score)

print(max(scenic))
