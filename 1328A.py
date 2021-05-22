n = int(input())
for i in range(0, n):
    c = [int(item) for item in input().split(" ")]
    if c[0] % c[1] == 0:
        print(0)
    else:
        print(c[1] - c[0] % c[1])