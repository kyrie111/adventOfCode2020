def day9_1():
    nums = [int(x) for x in open("num9.txt").read().split("\n") if x]
    for i in range(25, len(nums)):
        pn = set(nums[i - 25:i])
        for num in pn:
            if nums[i] - num in pn:
                break
        else:
            return nums[i]


def day9_2():
    cn = day9_1()
    nums = [int(x) for x in open("num9.txt").read().split("\n") if x]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            pn = nums[i:j]
            if sum(pn) == cn:
                return max(pn) + min(pn)


if __name__ == '__main__':
    print(day9_1())
    print(day9_2())
