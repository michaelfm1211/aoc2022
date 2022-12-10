hist = [1]
for line in open('ex'):
    cmd = line.strip().split(' ')
    if cmd[0] == 'noop':
        hist.append(hist[-1])
    else:
        hist.append(hist[-1])
        hist.append(hist[-1] + int(cmd[1]))

s = 0
for i in range(20, 220 + 40, 40):
    s += hist[i-1] * i
    # hist[i-1] because hist[i] contains result AFTER op,
    # but during the op is the same as before the op
print(s)
