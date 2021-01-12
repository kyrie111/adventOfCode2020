import string

data = []
for line in open('num6.txt', 'r'):
    data.append(line[:-1])

data1 = []
data1.append('')
n = 0
for i in data:
    if i == '':
        n += 1
        data1.append(i)
    else:
        data1[n] = data1[n] + ' ' + i


# # ——————————part1————————————
# data2 = []
# for i in data1:
#     s = ''
#     for j in i:
#         if j not in s:
#             s += j
#     s = s.strip()
#     data2.append(s)
#
# le = 0
# for i in data2:
#     le += i.__len__()
# print(le)

# ——————————part2————————————
data3 = []
res = 0
for i in data1:
    i = i.lstrip()
    j = i.split(' ')
    t = 0
    for c in string.ascii_lowercase:
        n = len(list(filter(lambda x: x.find(c) != -1, j)))
        if n == j.__len__():
            t += 1
    res += t
print(res)
