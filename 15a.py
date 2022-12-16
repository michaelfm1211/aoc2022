import re

sensors = []
beacons = []
for line in open('in'):
    n = list(map(int, re.findall('-?[0-9]+', line)))
    dist = abs(n[0] - n[2]) + abs(n[1] - n[3])
    sensors.append(((n[0], n[1]), dist))
    beacons.append((n[2], n[3]))

# line = 10
line = 2000000
taken = set()
for sensor in sensors:
    [pos, dist] = sensor
    if pos[1] + dist >= line and pos[1] - dist <= line:
        width = (2*dist+1) - 2*abs(line-pos[1])
        for d in range(pos[0]-width//2, pos[0]+width//2+1):
            taken.add(d)

taken -= set(map(lambda b: b[0], filter(lambda b: b[1] == line, beacons)))
print(len(taken))
