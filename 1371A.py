#-*- coding: utf- 8-*-
t = int(input())
answer = []
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        answer.append(n//2)
    else:
        answer.append((n + 1) // 2)
for i in range(t):
    print(answer[i])