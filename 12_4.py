data = []
for line in open('num4.txt', 'r'):
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

# ——————————part1————————————
# num = 0
# for i in data1:
#     i = i[1:i.__len__()]
#     info = i.split(' ')
#     print(info)
#     byr, iyr, eyr, hgt, hcl, ecl, pid, cid = 0, 0, 0, 0, 0, 0, 0, 0
#     for j in info:
#         x = j[0:3]
#         if x == 'byr':
#             byr = 1
#         elif x == 'iyr':
#             iyr = 1
#         elif x == 'eyr':
#             eyr = 1
#         elif x == 'hgt':
#             hgt = 1
#         elif x == 'hcl':
#             hcl = 1
#         elif x == 'ecl':
#             ecl = 1
#         elif x == 'pid':
#             pid = 1
#         elif x == 'cid':
#             cid = 1
#     t = byr + iyr + hgt + hcl + ecl + pid + cid + eyr
#     if t == 8 or (t == 7 and cid == 0):
#         num += 1
#
# print(num)

# ——————————part2————————————
num1 = 0
for i in data1:
    i = i[1:i.__len__()]
    info = i.split(' ')
    byr, iyr, eyr, hgt, hcl, ecl, pid, cid = 0, 0, 0, 0, 0, 0, 0, 0
    byr_v, iyr_v, eyr_v, hgt_v, hcl_v, ecl_v, pid_v, cid_v = '', '', '', '', '', '', '', ''
    print(i)
    for j in info:
        x = j[0:3]
        if x == 'byr':
            byr = 1
            byr_v = j[4:]
        elif x == 'iyr':
            iyr = 1
            iyr_v = j[4:]
        elif x == 'eyr':
            eyr = 1
            eyr_v = j[4:]
        elif x == 'hgt':
            hgt = 1
            hgt_v = j[4:]
        elif x == 'hcl':
            hcl = 1
            hcl_v = j[4:]
        elif x == 'ecl':
            ecl = 1
            ecl_v = j[4:]
        elif x == 'pid':
            pid = 1
            pid_v = j[4:]
        elif x == 'cid':
            cid = 1
            cid_v = j[4:]
    t = byr + iyr + hgt + hcl + ecl + pid + cid + eyr
    if t == 8 or (t == 7 and cid == 0):
        print(byr_v, iyr_v, eyr_v, hgt_v, hcl_v, ecl_v, pid_v, cid_v)
        if int(byr_v) < 1920 or int(byr_v) > 2002:
            continue

        if int(iyr_v) < 2010 or int(iyr_v) > 2020:
            continue

        if int(eyr_v) < 2020 or int(eyr_v) > 2030:
            continue

        # if hgt_v[-2:] != 'cm' or hgt_v[-2:] != 'in':
        #     continue

        if hgt_v[-2:] == 'cm':
            hgt_v_n = hgt_v[:-2]
            if int(hgt_v_n) < 150 or int(hgt_v_n) > 193:
                continue
        elif hgt_v[-2:] == 'in':
            hgt_v_n = hgt_v[:-2]
            if int(hgt_v_n) < 59 or int(hgt_v_n) > 76:
                continue

        if hcl_v[0:1] != '#':
            continue
        if hcl_v[1:].__len__() != 6:
            continue
        for m in hcl_v[1:]:
            if m.isalpha() and m > 'f':
                continue

        color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if ecl_v not in color:
            continue

        if pid_v.__len__() != 9:
            continue

        num1 += 1

print(num1)
