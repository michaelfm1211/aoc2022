alpha = 'abcdefghijklmnopqrstuvwxyz'
priority = {ch: i for (i, ch) in enumerate([0, *alpha, *alpha.upper()])}

priosum = 0
with open('input.txt') as f:
    for line in f.readlines():
        half = int(len(line) / 2)
        (ch,) = set(line[:half]).intersection(line[half:])
        priosum += priority[ch]
print(priosum)
