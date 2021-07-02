t = int(input())
n = []
for i in range(t):
    n.append(int(input()))
for p in n:
    for i in range(1, p + 1):
        print(i, end = " ")
    print("")