data = open('in').readline().strip()
for i in range(13, len(data)):
    frameSet = set(data[i-13:i+1])
    if len(frameSet) == 14:
        print(i + 1)
        break
