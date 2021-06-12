# -*- coding: utf- 8-*-
n = int(input())
answer = []
for i in range(n):
    x = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    a.sort()
    b.sort(reverse=True)
    for j in range(x[1]):
        if a[j] < b[j]:
            a[j], b[j] = b[j], a[j]
        else: break
    answer.append(a)
for i in range(n):
    sum = 0
    for j in answer[i]:
        sum += j
    print(sum)