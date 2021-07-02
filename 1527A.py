import math
t = int(input())
answer = []
for i in range(t):
    n = int(input())
    answer.append(math.pow(2,math.floor(math.log(n,2))) - 1)
for k in answer:
    print(int(k))