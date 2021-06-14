#-*- coding: utf- 8-*-
t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    count = 0
    for j in range(n):
        if a[j] - min(a) > b[j] - min(b):
            count += a[j] - min(a)
        else:
            count += b[j] - min(b)
    answers.append(count)
for i in range(t):
    print(answers[i])