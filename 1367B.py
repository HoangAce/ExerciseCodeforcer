#-*- coding: utf- 8-*-
t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    even = 0
    odd = 0
    for j in range(n):
        if j % 2 == 0 and a[j] % 2 == 1:
            even += 1
        if j % 2 == 1 and a[j] % 2 == 0:
            odd += 1
    if even == odd:
        answers.append(even)
    else:
        answers.append(-1)
for i in range(t):
    print(answers[i])