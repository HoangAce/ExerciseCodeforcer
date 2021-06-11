#-*- coding: utf- 8-*-
n = int(input())
numbers = list(map(int, input().split(" ")))
sum = 0
count = 0
for i in numbers:
    sum += i
    if sum < 0:
        sum = 0
        count += 1
print(count)