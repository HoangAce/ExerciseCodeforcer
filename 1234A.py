import  math
answer = []
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    answer.append(math.ceil(sum(a)/n))
for i in answer:
    print(i)