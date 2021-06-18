def dequy(n,m):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    return max(n, m) //2 * min (n,m) + dequy(max(n, m) % 2, min(n,m))
t = int(input())
answer = []
for i in range(t):
    a  = list(map(int, input().split(" ")))
    answer.append(dequy(a[0], a[1]))
for i in answer:
    print(i)