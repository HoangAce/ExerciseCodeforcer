t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for ai in range(n - 1):
        for aii in range(ai + 1, n):
            if(a[ai] % 2 == 0 and a[aii] % 2 == 1):
                a[ai], a[aii] = a[aii], a[ai]
                break
    answers.append(a)
for answer in answers:
    print(' '.join(str(a) for a in answer))