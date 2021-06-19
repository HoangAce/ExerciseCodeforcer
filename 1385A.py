t = int(input())
answer = []
xyz = []
for i in range(t):
    x = list(map(int, input().split(" ")))
    x.sort()
    xyz.append(x)
for i in xyz:
    if i[2] ==  i[1] >= i[0]:
        print("YES")
        print(i[2], i[0], 1)
    else:
        print("NO")
