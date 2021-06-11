#-*- coding: utf- 8-*-
number = list(map(int, input().split(" ")))
str1 = ""
for i in range(len(number)):
    if i != number.index(max(number)):
        str1 = str1 + str(max(number) - number[i]) + " "
print(str1)