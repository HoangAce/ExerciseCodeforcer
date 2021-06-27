import math
t = int(input())
answer = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    count = 0
    for i in range(n - 1):
        if max(a[i],a[i + 1]) > 2 * min(a[i],a[i + 1]):
            count += math.floor(math.log(math.ceil(max(a[i],a[i + 1]) / min(a[i],a[i + 1])) - 1,2))
    answer.append(count)
for i in answer:
    print(i)