# -*- coding: utf- 8-*-
t = input().split(" ")
n = int(t[0])
k = int(t[1])
sum = 0
for i in range(n + 1):
    sum = sum + i * 5
    if sum + k > 240 :
       n = i - 1  
       break
print(n)