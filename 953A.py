import math
n = int(input())
check = 1
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if n / i == i:
            check += 1
        else: check += 2
print(check)