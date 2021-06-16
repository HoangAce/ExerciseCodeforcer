#-*- coding: utf- 8-*-
t = int(input())
answer = []
for i in range(t):
    n = int(input())
    p = list(input().split(" "))
    po = [p[0]]
    check = 0
    for i in p:
        if p.index(i) > check:
            po.append(i)
            check = p.index(i)
    answer.append(po)
for i in answer:
    for j in i:
        print(j, end = " ")
    print("")

