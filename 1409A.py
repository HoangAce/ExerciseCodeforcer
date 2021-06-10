#-*- coding: utf- 8-*-
import  math
a = []
t = int(input())
for i in range(t):
    a.append (list(input().split(" ")))
for i in range(t):
    print(math.ceil(abs(int(a[i][0]) - int(a[i][1])) / 10))