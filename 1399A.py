# -*- coding: utf- 8-*-
t = int(input())
n = []
a = []
for i in range(t):
    n.append(int(input()))
    a.append(list(map(lambda x: int(x), input().split(" "))))
for i in range(t):
    answer = "YES"
    a[i].sort()
    for j in range(n[i] - 1):
        if (int(a[i][j + 1]) - int(a[i][j])) > 1 :
            answer = "NO"
            break
    print(answer)