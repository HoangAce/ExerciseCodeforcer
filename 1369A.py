n = int(input())
answer = []
for i in range(t):
    n = int(input())
    if n % 4 == 0:
        answer.append("YES")
    else:
        answer.append("NO")
for i in answer:
    print(i)
