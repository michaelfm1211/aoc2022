alpha = 'abcdefghijklmnopqrstuvwxyz'
priority = {ch: i for (i, ch) in enumerate([0, *alpha, *alpha.upper()])}

priosum = 0
with open('input.txt') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        s = list(set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2]))
        s.remove('\n')
        priosum += priority[s[0]]
print(priosum)
