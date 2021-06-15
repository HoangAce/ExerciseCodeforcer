#-*- coding: utf- 8-*-
t = int(input())
answer = []
for i in range(t):
    n = list(map(int, input().split(" ")))
    if n[0] == 1:
        answer.append(0)
    elif n[0] == 2:
        answer.append(n[1])
    else :
        answer.append(n[1] * 2)
for i in range(t):
    print(answer[i])