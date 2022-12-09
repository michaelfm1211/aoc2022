class Node:
    def __init__(self, parent, name='/'):
        self.parent = parent
        self.children = {}

    def size(self):
        total = 0
        for el in self.children.values():
            if type(el) == int:
                total += el
            elif type(el) == Node:
                total += el.size()
        return total

    def get(self, path):
        path = path.split('/')
        if len(path) == 1:
            return self.children[path[0]]
        return self.children[path[0]].get(path[1:])

    def addDir(self, name):
        self.children[name] = Node(self)

    def addFile(self, name, size):
        self.children[name] = size

    def ans(self):
        res = 0
        for el in self.children.values():
            if type(el) == Node:
                s = el.size()
                res += s if s <= 100000 else 0
                res += el.ans()
        return res

    def __repr__(self):
        return f"({self.size()}, {self.children})"


root = Node(None)
cwd = root
for line in open('in'):
    cmd = line.strip().split(' ')
    if cmd[0] == '$':  # command
        if cmd[1] == 'cd':
            if cmd[2] == '/':
                cwd = root
            elif cmd[2] == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.get(cmd[2])
    else:  # file listing
        if cmd[0] == 'dir':
            cwd.addDir(cmd[1])
        else:
            cwd.addFile(cmd[1], int(cmd[0]))

ans = root.ans()
s = root.size()
if s <= 1000000:
    ans += s
print(ans)
