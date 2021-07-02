t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if max(a) == min(a):
        answers.append(0)
    elif sum(a) % n == 0:
        count = 0
        tb = sum(a) / n
        for i in range(n):
            if a[i] > tb:
                count += 1
        answers.append(count)
    else:
        answers.append(-1)
for answer in answers:
    print (answer)
