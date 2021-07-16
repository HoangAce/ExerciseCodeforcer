import math
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for b in  a:
        if not(math.sqrt(b).is_integer()):
            print("YES")
            break
    else: 
        print("NO")