t = int(input())
answers = []
for i in range(t):
    x = ""
    y = ""
    p = list(map(int,input().split()))
    S = input()
    if p[0] > 0:
        x = "R"
    else:
        x = "L"
        p[0] = -p[0]
    if p[1] > 0:
        y = "U"
    else:
        y = "D"
        p[1] = -p[1]
    for char in S:
        if p[0] != 0 and char == x:
            p[0] -= 1
        elif p[1] != 0 and char == y:
            p[1] -= 1
        if p[0] == 0 and p[1] == 0:
            answers.append("YES")
            break
    else: answers.append("NO")
for answer in answers:
    print(answer)