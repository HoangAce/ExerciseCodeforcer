# -*- coding: utf- 8-*-
n = int(input())
t = list(map(int, input().split(" ")))
t1 = []
t2 = []
t3 = []
for i in range(n):
    if t[i] == 1: t1.append(i + 1)
    elif t[i] == 2: t2.append(i + 1)
    else: t3.append(i + 1)
count = min(len(t1), len(t2), len(t3))
print(count)
if count > 0:
    for i in range(count):
        print(t1[i], t2[i], t3[i])