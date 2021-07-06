t = int(input())
answers = []
for i in range(t):
    vertices = list(map(int, input().split()))
    if vertices[0] % vertices[1] == 0:
        answers.append("YES")
    else:
        answers.append("NO")
for answer in answers:
    print(answer)