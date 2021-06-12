# -*- coding: utf- 8-*-
n = int(input())
a = list(map(int, input().split(" ")))
count = 0
for i in range(n):
    count += max(a) - a[i]
print(count)