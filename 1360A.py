#-*- coding: utf- 8-*-
t = int(input())
hcn = []
for i in range(t):
    s = list(map(int, input().split(" ")))
    if 2 * min(s) > max(s):
        hcn.append(min(s) * min(s) * 4)
    else:
        hcn.append(max(s) * max(s))
for i in range(t):
    print(hcn[i])