def day15_1():
    inst = [int(x) for x in open("num15.txt").read().split(',') if x]
    inst.reverse()
    tc = len(inst) - 1
    while tc < 2020:
        try:
            inst.insert(0, inst[1:].index(inst[0]) + 1)
        except:
            inst.insert(0, 0)
        tc += 1

    return inst[1]


def day15_2():
    inst = [int(x) for x in open("num15.txt").read().split(',') if x]
    pos = {x: y for y, x in enumerate(inst[:-1])}
    tc = len(inst) - 1
    while tc < 30000000:
        inst.append(tc - pos.get(inst[-1], tc))
        pos[inst[-2]] = tc
        tc += 1

    return inst[-2]


print(day15_1())
print(day15_2())
