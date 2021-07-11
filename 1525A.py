def UCLN(x, y):
    if y == 0:
        return x
    return UCLN(y, x % y)
t = int(input())
arrK = []
for i in range(t):
    arrK.append(int(input()))
for k in arrK:
    print(100 // UCLN(100, k))