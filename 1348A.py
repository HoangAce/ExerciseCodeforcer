#-*- coding: utf- 8-*-
t = int(input())
answers = []
for i in range(t):
    n = int(input())
    answer = pow(2, n) - pow(2, n/2)
    for j in range(n//2 - 1):
        answer = answer + pow(2, j + 1)- pow(2, n - j - 1)
    answers.append(int(answer))
for i in range(t):
    print(answers[i])
