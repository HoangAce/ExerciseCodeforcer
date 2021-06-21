t = int(input())
LCM = []
for i in range(t):
    LCM.append(list(map(int, input().split(" "))))
for i in LCM:
    if i[0]  * 2 > i[1]:
        print(-1, -1)
    else:
        print(i[0], i[0] * 2)