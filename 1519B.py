t = int(input())
answers = []
for i in range(t):
    r = list(map(int, input().split()))
    if (r[0] * r[1] - 1) == r[2]:
        answers.append("YES")
    else:
        answers.append("NO")
for answer in answers:
    print(answer)