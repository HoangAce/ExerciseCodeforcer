t = int(input())
answer = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    if n == 1 or sum(a) % 2 == 1:
        answer.append("NO")
    elif 1 not in a and n % 2 == 1:
        answer.append("NO")
    else:
        answer.append("YES")
for i in answer:
    print(i)
