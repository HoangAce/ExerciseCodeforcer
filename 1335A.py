# -*- coding: utf- 8-*-
import math
n = []
t = int(input())
for i in range(t):
    n.append(int(input()))
for i in range(t):
    print(math.ceil(n[i] / 2) - 1)