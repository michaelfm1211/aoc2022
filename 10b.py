hist = [1]  # hist[i] is register x's value AFTER cycle i
for line in open('in'):
    cmd = line.strip().split(' ')
    if cmd[0] == 'noop':
        hist.append(hist[-1])
    else:
        hist.append(hist[-1])
        hist.append(hist[-1] + int(cmd[1]))

for i in range(240):
    pos = i % 40
    if pos == 0:
        print('\n', end='')

    x = hist[i]
    if pos >= x-1 and pos <= x+1:
        print('#', end='')
    else:
        print('.', end='')

print('\n')  # to look nice
