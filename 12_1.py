data = []
for line in open('adventOfCode2020/num1.txt','r'):
    data.append(line[:-1])

res = -1

len = data.__len__()
for i in range(len):
    for j in range(i+1, len):
        for x in range(j+1,len):
            if int(data[i]) + int(data[j]) + int(data[x]) == 2020:
                res = int(data[i]) * int(data[j]) * int(data[x])
                break

print(res)