t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for ai in a:
        if ai % 2 ==0:
            count += 1
        else:
            count -= 1
    if count == 0:
        answers.append("YES")
    else:
        answers.append("NO")
for answer in answers:
    print(answer)