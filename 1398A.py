t = int(input())
a = []
for i in range(t):
    n = int(input())
    a.append(list(map(int, input().split(" "))))
for ai in a:
    if ai[0] + ai[1] <= ai[-1]:
        print(1, 2, len(ai))
    else:
        print(-1)