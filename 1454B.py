t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = a.copy()
    b.sort()
    if n == 1:
        min = 1
    elif b[0] != b[1]:
        min = a.index(b[0]) + 1
    else:
        min = -1
        if n > 2:
            for i in range(2, n - 1):
                if b[i - 1] != b[i] !=b[i + 1]:
                    min = a.index(b[i]) + 1
                    break
            else:
                if b[n - 1] != b[n -2]:
                    min = a.index(b[n - 1]) + 1
    answers.append(min)
for answer in answers:
        print(answer)