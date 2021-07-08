t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] < a[i + 1]:
            answers.append(n - i - 1)
            break
    else: answers.append(0)
for answer in answers:
    print(answer)