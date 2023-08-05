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
    if name == 'humn':
        return 1j
    elif name == 'root':
        dep1 = evaluate_node(g[name]['deps'][0])
        dep2 = evaluate_node(g[name]['deps'][1])

        humn = dep1 if isinstance(dep1, complex) else dep2
        real = dep2 if isinstance(dep1, complex) else dep1

        return (real - humn.real) / humn.imag

    if 'val' in g[name]:
        return g[name]['val']
    else:
        dep1 = evaluate_node(g[name]['deps'][0])
        dep2 = evaluate_node(g[name]['deps'][1])

        op = g[name]['op']
        val = dep1
        if op == '+':
            val += dep2
        elif op == '-':
            val -= dep2
        elif op == '*':
            val *= dep2
        elif op == '/':
            val /= dep2
        g[name][val] = val
        return val


val = evaluate_node('root')
print(val)
