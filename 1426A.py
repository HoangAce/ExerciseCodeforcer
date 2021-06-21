import math
t = int(input())
answer = []
for i in range(t):
    n = list(map(int,input().split(" ")))
    if n[0] <= 2:
        answer.append(1)
    else:
        answer.append(math.ceil((n[0] - 2) / n[1]) + 1)
for i in answer:
    print(i)