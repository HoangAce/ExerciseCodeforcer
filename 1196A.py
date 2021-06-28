import math
q = int(input())
answer = []
for i in range(q):
    a = list(map(int, input().split(" ")))
    answer.append(sum(a)//2)
for i in answer:
    print(i)