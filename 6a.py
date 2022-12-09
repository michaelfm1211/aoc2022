data = open('in').readline().strip()
for i in range(3, len(data)):
    frameSet = set(data[i-3:i+1])
    if len(frameSet) == 4:
        print(i + 1)
        break
