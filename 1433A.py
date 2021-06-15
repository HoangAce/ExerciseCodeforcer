#-*- coding: utf- 8-*-
t = int(input())
answer = []
for i in range(t):
    x = input()
    count = 10 * (int(x[0]) - 1)
    for j in range(len(x)):
        count += 1 + j
    answer.append(count)
for i in range(t):
    print(answer[i])