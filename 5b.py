from collections import deque

lines = [line for line in open('in')]

stacks = [deque() for i in range(len(lines[0])//4)]

i = 0
while not lines[i].startswith(' 1'):
	for j in range(1, len(lines[i])-1, 4):
		if lines[i][j] not in '[] ':
			stacks[j//4].appendleft(lines[i][j])
	i += 1
i += 2

for j in range(i, len(lines)):
	cmd = lines[j].strip().split(' ')
	tmp = [stacks[int(cmd[3])-1].pop() for _ in range(int(cmd[1]))]
	tmp.reverse()
	stacks[int(cmd[5])-1].extend(tmp)

s = ""
for stack in stacks:
	s += stack.pop()
print(s)
