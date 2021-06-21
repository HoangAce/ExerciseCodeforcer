t = int(input())
arrA = []
for i in range(t):
    n =  int(input())
    b = list(map(int, input().split(" ")))
    a = b.copy()
    for j in range(n):
        if j % 2 == 0:
            a[j] = b[j // 2]
        else:
            a[j] = b[n - (j + 1) // 2]
    arrA.append(a)
for ais in arrA:
    for ai in ais:
        print(ai, end = " ")
    print("")