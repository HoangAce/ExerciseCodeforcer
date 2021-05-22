n = int(input())
c = list()
count = 0
for i in range(0, n):
    c += [int(item) for item in input().split(" ")]
for i in range(0, n):
    for j in range(0,n):
        if 2 * i + 1 != 2 * j + 1 and c[2 * i] == c[2 * j + 1]:
            count += 1
print(count)
