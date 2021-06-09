# -*- coding: utf- 8-*-
n = int(input())
t = input().split(" ")
max = int(t[0])
min = int(t[0])
sum = 0
for i in range(n):
    if (int(t[i]) > max):
        sum += 1
        max = int(t[i])
    if (int(t[i]) < min):
        sum += 1
        min = int(t[i])
print(sum)