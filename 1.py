def nmax(itr, n):
    res = [0] * n
    low = 0
    for el in itr:
        if el > low:
            res.remove(low)
            res.append(el)
            low = min(res)
    return res


with open('test.txt') as f:
    elves = [0]
    for line in f.readlines():
        if line == '\n':
            elves.append(0)
            continue
        elves[-1] += int(line)
    top = nmax(elves, 3)
    print(sum(top))
