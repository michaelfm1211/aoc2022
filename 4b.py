lines = [line.strip() for line in open('in')]
# lines = [line.strip() for line in open('ex')]

cnt = 0
for line in lines:
    [a, b] = line.split(',')
    [a1, a2] = [int(x) for x in a.split('-')]
    [b1, b2] = [int(x) for x in b.split('-')]

    if not a2 < b1 and not b2 < a1:
        cnt += 1
print(cnt)
