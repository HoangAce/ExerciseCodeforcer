n = int(input())
x = list(input().split(" "))
y = list(input().split(" "))
p = set(x[1:])
p.update(y[1:])
if len(p) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")