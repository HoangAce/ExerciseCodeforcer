import math
count = 0
[n, m] = list(map(int, input().split()))
test = math.floor(math.sqrt(n)) + 1
for i in range(test):
    if i + pow((n - pow(i, 2)), 2) == m:
        count += 1
print(count)