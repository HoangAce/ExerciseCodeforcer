a = list(map(int, input().split(" ")))
s = input()
calo = 0
for i in s:
    calo += a[int(i) - 1]
print(calo)