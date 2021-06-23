t = int(input())
answer = []
for i in range(t):
    n = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    min1 = min(a)
    a.remove(min(a))
    min2 = min(a)
    if max(a) <= n[1] or (min1 + min2) <= n[1]:
        answer.append("YES")
    else:
        answer.append("NO")
for i in answer:
    print(i)