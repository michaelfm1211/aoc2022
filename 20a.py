import collections

# uniq_id is just to make every object unique
vals = [{'seen': False, 'val': int(line.strip()), 'uniq_id': i}
        for i, line in enumerate(open('20.txt'))]

q = collections.deque(vals)
while q:
    obj = q.popleft()
    if obj['seen']:
        continue

    i = vals.index(obj)
    del vals[i]

    new_i = (i + obj['val']) % len(vals)
    if new_i == 0:
        new_i = len(vals)  # quirk in question, the the edge must be in back

    vals.insert(new_i, obj)


nums = [obj['val'] for obj in vals]
zero_i = nums.index(0)
x = nums[(zero_i + 1000) % len(vals)]
y = nums[(zero_i + 2000) % len(vals)]
z = nums[(zero_i + 3000) % len(vals)]
print(x + y + z)
