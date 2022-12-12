class Monkey:
    def __init__(self, items, rule, divTest, trueRes, falseRes):
        self.items = items
        self.rule = rule
        self.divTest = divTest
        self.trueRes = trueRes
        self.falseRes = falseRes
        self.count = 0

    def __repr__(self):
        return f'  {self.items}'


data = open('in').read()
monkeys = []
for monkey in data.split('\n\n'):
    lines = monkey.split('\n')

    items = list(map(int, lines[1][18:].split(', ')))
    rule = lines[2][19:]
    divTest = int(lines[3][21:])
    trueRes = int(lines[4][29:])
    falseRes = int(lines[5][30:])

    monkeys.append(Monkey(items, rule, divTest, trueRes, falseRes))

for i in range(20):
    for monkey in monkeys:
        items = [*monkey.items]
        for item in items:
            monkey.count += 1
            monkey.items.remove(item)
            item = eval(monkey.rule, {'old': item})//3
            if item % monkey.divTest == 0:
                monkeys[monkey.trueRes].items.append(item)
            else:
                monkeys[monkey.falseRes].items.append(item)
                
vals = sorted(monkeys, key=lambda m: m.count)
print(vals[-1].count * vals[-2].count)
