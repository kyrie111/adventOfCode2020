data = []
with open('num3.txt', 'r') as f:
    my_data = f.readlines()
    for line in my_data:
        line_data = list(line)[:-1]
        data.append(line_data)

hight = data.__len__()
width = data[0].__len__()
print(hight, width)

# right 3, down 1
tree_num1 = 0
for i in range(hight):
    if i == 0:
        j = 0
    elif i <= (width / 3):
        j = i * 3
    else:
        j = (i * 3) % width
    if data[i][j] == '#':
        tree_num1 += 1
print(tree_num1)

# right 1, down 1
tree_num2 = 0
for i in range(hight):
    if i == 0:
        j = 0
    # elif i <= (width/1):
    #     j = i * 1
    else:
        j = (i * 1) % width
    if data[i][j] == '#':
        tree_num2 += 1
print(tree_num2)

# right 5, down 1
tree_num3 = 0
for i in range(hight):
    if i == 0:
        j = 0
    elif i <= (width / 5):
        j = i * 5
    else:
        j = (i * 5) % width
    if data[i][j] == '#':
        tree_num3 += 1
print(tree_num3)

# right 7, down 1
tree_num4 = 0
for i in range(hight):
    if i == 0:
        j = 0
    elif i <= (width / 7):
        j = i * 7
    else:
        j = (i * 7) % width
    if data[i][j] == '#':
        tree_num4 += 1
print(tree_num4)

# right 1, down 2
tree_num5 = 0
for i in range(hight):
    if i % 2 == 1:
        continue
    if i == 0:
        j = 0
    # elif i <= (width/5):
    #     j = i * 5
    else:
        j = (i * 1) % width
    if data[i][j] == '#':
        tree_num5 += 1
print(tree_num5)

print(tree_num1*tree_num2*tree_num3*tree_num4*tree_num5)
