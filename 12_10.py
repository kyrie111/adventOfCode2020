from utils import *

inp = """
26
97
31
7
2
10
46
38
112
54
30
93
18
111
29
75
139
23
132
85
78
99
8
113
87
57
133
41
104
98
58
90
13
91
20
68
103
127
105
114
138
126
67
32
145
115
16
141
1
73
45
119
51
40
35
150
118
53
80
79
65
135
74
47
128
64
17
4
84
83
147
142
146
9
125
94
140
131
134
92
66
122
19
86
50
52
108
100
71
61
44
39
3
72"""

inp2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

nums = [int(i) for i in inp.split()]

builtin = max(nums) + 3

nums = sorted(nums) + [builtin]

c = 0
ones = 0
threes = 0
for n in nums:
    if n - c == 1:
        ones += 1
    elif n - c == 3:
        threes += 1
    c = n

print(ones * threes)

cache = {}

def arrangements(adapters):
    tgt = adapters[-1]
    if tgt in cache:
        return cache[tgt]

    if tgt == 0:
        return 1
    srcs = [a for a in adapters[-4:] if 1 <= tgt - a <= 3]
    ans = sum([arrangements([a for a in adapters if a <= s]) for s in srcs])
    cache[tgt] = ans
    return ans


arrs = arrangements([0] + nums)
print(arrs)