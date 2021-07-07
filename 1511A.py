t = int(input())
answers = []
for i in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    count = 0
    for i in r:
        if i == 1 or i == 3:
            count += 1
    answers.append(count)
for answer in answers:
    print(answer)