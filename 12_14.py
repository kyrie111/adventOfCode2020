import re


def day14_1():
    inst = [x for x in open("num14.txt").read().split("\n") if x]
    mem = dict()
    for line in inst:
        if line.startswith("mask"):
            mask = line.split("= ")[1]
            continue
        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        memid, value = m.groups()
        nv = list(bin(int(value))[2:].zfill(len(mask)))
        for i in range(len(mask) - 1, -1, -1):
            if mask[i] == 'X':
                continue
            nv[i] = mask[i]

        mem[memid] = int("".join(nv), 2)

    return sum(mem.values())


def day14_2():
    inst = [x for x in open("num14.txt").read().split("\n") if x]
    mem = dict()
    for line in inst:
        if line.startswith("mask"):
            mask = line.split("= ")[1]
            dmasks = list(mask)
            xs = mask.count('X')
            masks = []
            # print("MK" + mask)
            for i in range(2 ** xs):
                vs = list(bin(i)[2:].zfill(xs))
                # print("".join(vs))
                dupe = dmasks.copy()
                for j, c in enumerate(dupe):
                    if c == 'X':
                        dupe[j] = str(int(vs.pop(0)) + 2)

                # print("".join(dupe))
                masks.append("".join(dupe))

            continue

        m = re.match(r"mem\[(\d+)\] = (\d+)", line)
        memid, value = m.groups()
        # print('M', bin(int(memid))[2:].zfill(len(mask)))
        for dmask in masks:
            nv = list(bin(int(memid))[2:].zfill(len(dmask)))
            for ir in range(len(dmask) - 1, -1, -1):
                if dmask[ir] == '0':
                    continue
                if dmask[ir] == '1':
                    nv[ir] = dmask[ir]
                if dmask[ir] == '2':
                    nv[ir] = '0'
                if dmask[ir] == '3':
                    nv[ir] = '1'

            # print('V', "".join(nv))
            mem[int("".join(nv), 2)] = int(value)

    # print(mem)
    return sum(mem.values())

print(day14_1())
print(day14_2())