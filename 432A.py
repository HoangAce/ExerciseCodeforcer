# -*- coding: utf- 8-*-
x = list(map(int, input().split(" ")))
y = list(map(int, input().split(" ")))
count = 0
for i in range(x[0]):
    if(y[i] <= 5 - x[1]):
        count += 1
print(count // 3)