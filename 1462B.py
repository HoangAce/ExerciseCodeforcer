t = int(input())
answers = []
for i in range(t):
    n = int(input())
    S = input()
    for j in range(5):
        if S[0:j] + S[n - 4 + j: n] == "2020":
            answers.append("YES")
            break
    else:
        answers.append("NO")
for answer in answers:
    print(answer)