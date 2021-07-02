d = list(map(int, input().split()))
if d[0] + d[1] <= d[2]:
    print(2 * (d[0] + d[1]))
elif d[0] + d[2] <= d[1]:
    print(2 * (d[0] + d[2]))
elif d[1] + d[2] <= d[0]:
    print(2 * (d[1] + d[2]))
else:
    print(sum(d))
