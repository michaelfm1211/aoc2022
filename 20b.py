import collections


decrypt_key = 811589153


def mix(vals):
    q = collections.deque(vals)
    while q:
        obj = q.popleft()
        if obj['seen']:
            continue

        i = vals.index(obj)
        del vals[i]

        new_i = (i + obj['val']) % len(vals)
        if new_i == 0 and obj['val'] != 0:
            # quirk in question, the the edge must be in back
            new_i = len(vals)
        # print('??', obj['val'], 'at', i, 'is now at', new_i)

        vals.insert(new_i, obj)


# uniq_id is just to make every object unique
vals = [{'seen': False, 'val': int(line.strip()) * decrypt_key, 'uniq_id': i}
        for i, line in enumerate(open('20test.txt'))]

for i in range(10):
    mix(vals)
    nums = [obj['val'] for obj in vals]
    print(i + 1, nums)

nums = [obj['val'] for obj in vals]
print(nums)
zero_i = nums.index(0)
x = nums[(zero_i + 1000) % len(vals)]
y = nums[(zero_i + 2000) % len(vals)]
z = nums[(zero_i + 3000) % len(vals)]
print(x, y, z, x + y + z)
