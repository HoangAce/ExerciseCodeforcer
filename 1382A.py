t = int(input())
a = []
b = []
for i in range(t):
    n = input()
    a.append(list(map(int, input().split(" "))))
    b.append(list(map(int, input().split(" "))))
for i in range(t):
    for j in a[i]:
        if j in b[i]:
            print("YES")
            print(1, j)
            break
    else: print("NO")