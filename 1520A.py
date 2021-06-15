#-*- coding: utf- 8-*-
t = int(input())
answer = []
for i in range(t):
    n = int(input())
    Po = input()
    index = []
    temp = 0
    for i in Po:
        index.append(Po.index(i))
    for i in range(n - 1):
        if index[i] > index[i + 1]:
            temp += 1
    if temp > 0:
        answer.append("NO")
    else:
            answer.append("YES")
for i in range(t):
    print(answer[i])