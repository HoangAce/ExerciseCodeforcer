n = list(map(int, input().split()))
count = 0
for i in range(n[0]):
    d = list(input().split())
    if d[0] == "+":
        n[1] += int(d[1])
    elif n[1] >= int(d[1]):
            n[1] -=int(d[1])
    else: count += 1
print(n[1],count)