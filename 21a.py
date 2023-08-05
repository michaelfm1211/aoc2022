# parse input
g = {}
for line in open('21.txt'):
    name, calc = line.strip().split(': ')
    if calc.isdigit():
        g[name] = {'val': int(calc)}
    else:
        dep1, op, dep2 = calc.split(' ')
        g[name] = {'op': op, 'deps': [dep1, dep2]}


def evaluate_node(name):
    print(name)
    if 'val' in g[name]:
        return g[name]['val']
    else:
        dep1 = evaluate_node(g[name]['deps'][0])
        dep2 = evaluate_node(g[name]['deps'][1])
        op = g[name]['op']

        g[name]['val'] = eval(f'{dep1} {op} {dep2}')
        return g[name]['val']


val = evaluate_node('root')
print(val)
