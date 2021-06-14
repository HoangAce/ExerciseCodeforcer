#-*- coding: utf- 8-*-
t = int(input())
answers = []
for i in range(t):
    n = int(input())
    s = list(map(int, input().split(" ")))
    s.sort()
    min = s[1] - s[0]
    for j in range(n - 1):
        if(s[j+1] - s[j]) < min:
            min = s[j+1] - s[j]
    answers.append(min)
for i in range(t):
    print(answers[i])