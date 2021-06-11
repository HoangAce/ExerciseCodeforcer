#-*- coding: utf- 8-*-
t = int(input())
strings =[]
for i in range(t):
    strings.append(input())
for string in strings:
    b = string[0]
    for index, value in enumerate(string):
        if index % 2 == 1:
            b += value
    print(b)
    