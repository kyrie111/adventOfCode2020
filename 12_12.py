import numpy as np


def day12_1():
    instructions = open("num12.txt").read().split()
    cpos = np.array([0, 0])
    dir = np.e ** (1j * np.pi)
    for (inst, *rest) in instructions:
        if inst == "W":
            cpos[0] += int("".join(rest))
        elif inst == "E":
            cpos[0] -= int("".join(rest))
        elif inst == "N":
            cpos[1] += int("".join(rest))
        elif inst == "S":
            cpos[1] -= int("".join(rest))

        elif inst == "F":
            amt = int("".join(rest))
            cpos += [int(dir.real) * amt, int(dir.imag) * amt]
        elif inst == "L":
            dir /= np.e ** (1j * int("".join(rest)) / 180 * np.pi)
        elif inst == "R":
            dir *= np.e ** (1j * int("".join(rest)) / 180 * np.pi)

    return abs(int(cpos[0])) + abs(int(cpos[1]))


import math


def day12_2():
    instructions = [x for x in open("num12.txt").read().split() if x]
    ship = np.array([0., 0.])
    wayp = np.array([-10., 1.])
    for (inst, *rest) in instructions:
        if inst == "W":
            wayp[0] += int("".join(rest))
        elif inst == "E":
            wayp[0] -= int("".join(rest))
        elif inst == "N":
            wayp[1] += int("".join(rest))
        elif inst == "S":
            wayp[1] -= int("".join(rest))

        elif inst == "F":
            amt = int("".join(rest))
            ship += amt * wayp
        elif inst == "L":
            ang = -int("".join(rest)) * np.pi / 180
            dp = np.linalg.norm(wayp) * np.e ** (1j * (ang + math.atan2(wayp[1], wayp[0])))
            wayp[:] = round(dp.real), round(dp.imag)
        elif inst == "R":
            ang = int("".join(rest)) * np.pi / 180
            dp = np.linalg.norm(wayp) * np.e ** (1j * (ang + math.atan2(wayp[1], wayp[0])))
            wayp[:] = round(dp.real), round(dp.imag)

    return abs(int(ship[0])) + abs(int(ship[1]))


if __name__ == '__main__':
    print(day12_1())
    print(day12_2())
