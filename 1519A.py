t = int(input())
answers = []
for i in range(t):
    n = list(map(int, input().split()))
    if abs(n[0] - n[1]) <= n[2] * min(n[0], n[1]):
        answers.append("YES")
    else:
        answers.append("NO")
for answer in answers:
    print (answer)
