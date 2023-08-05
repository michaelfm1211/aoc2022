'''
  [-1] [ 2] [ 2] [-1] [ 0]
+ [ 0] [ 1] [ 2] [-2] [ 1]
==========================
  [-1] [ 3] [ 4] [-3] [ 1]
  1 + -3(5) + 4(25) + 3(125) + -1(625)
  carry over in multiples of 5, even if that makes it negative
1 1 + -3(5) + 4(25) + 3(125) + -1(625)
2 1 + 2(5) + 3(25) + 3(125) + -1(625)
3 1 + 2(5) + -2(25) + 4(125) + -1(625)
4 1 + 2(5) + -2(25) + -1(125) + 0(625)

  [ x] [ x] [ x] [ x] [ x]
'''


# add two SNAFU value lists
def add_values(vals1, vals2):
    # pad the lists
    while len(vals1) < len(vals2):
        vals1.insert(0, 0)
    while len(vals2) < len(vals1):
        vals2.insert(0, 0)

    # add element-wise
    return [vals1[i] + vals2[i] for i in range(len(vals1))]


# carry over values by subtracting or adding in one higher powers
def carry(vals):
    for i in range(len(vals) - 1, 0, -1):
        while vals[i] > 2:
            vals[i] -= 5
            try:
                vals[i - 1] += 1
            except IndexError:
                vals.insert(0, 1)

        while vals[i] < -2:
            vals[i] += 5
            try:
                vals[i - 1] -= 1
            except IndexError:
                vals.insert(0, 1)


# Translate from SNAFU symbols to SNAFU value lists
trans = ['=', '-', '0', '1', '2']  # translation array
values = []
for line in open('25.txt'):
    value = [trans.index(ch) - 2 for ch in line.strip()]
    values.append(value)

# Add together all SNAFU value lists into a sum SNAFU value list
total = [0]
for value in values:
    total = add_values(total, value)

# Carry over the values
carry(total)

# Translate from SNAFU value list to SNAFU symbols
snafu = ''.join(trans[val + 2] for val in total)
print(snafu)
