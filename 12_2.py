data = []
for line in open('adventOfCode2020/num2.txt', 'r'):
    data.append(line[:-1])
res = 0
len = data.__len__()


# for i in range(len):
#     s = data[i].split(' ')
#     num = s[0].split('-')
#     min = int(num[0])
#     max = int(num[1])
#     ch = s[1][:-1]
#     n = 0
#     for j in s[2]:
#         if j == ch:
#             n = n + 1
#     if (n >= min) and (n <= max):
#         res = res + 1


# ——————————part2————————————
for i in range(len):
    s = data[i].split(' ')
    num = s[0].split('-')
    min = int(num[0])
    max = int(num[1])
    ch = s[1][:-1]
    n = 0
    x = (s[2][min - 1] == ch)
    y = (s[2][max - 1] == ch)
    if (x == True) and (y == True):
        continue
    if x or y:
        res = res + 1

print(res)
