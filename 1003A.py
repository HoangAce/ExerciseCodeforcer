n = int(input())
a = list(map(int, input().split()))
aSet = set(a)
max = 0
for item in aSet:
    count = a.count(item)
    if count > max:
        max = count
print(max) 