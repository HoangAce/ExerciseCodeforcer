import math
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n = int(input())
if n >= (math.ceil(sum(a) / 5) + math.ceil(sum(b) / 10)):
    print("YES")
else:
    print("NO")