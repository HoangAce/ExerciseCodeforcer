t = int(input())
answers = []
for i in range(t):
    n = list(map(int, input().split()))
    if min(n) == 1:
        answers.append("YES")
    elif max(n) > 2:
        answers.append("NO")
    else:
        answers.append("YES")
for answer in answers:
    print(answer)