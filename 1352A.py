# -*- coding: utf- 8-*-
t = int(input())
n = []
for i in range(t):
    number = input()
    answer = set()
    for count, item in enumerate(number):
        if item != '0':
            answer.add(item + '0' * (len(number) - 1 - count))
    n.append(answer)
for i in range(t):
    print(len(n[i]))
    print(" ".join(n[i]))