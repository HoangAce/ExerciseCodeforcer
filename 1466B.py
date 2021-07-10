t = int(input())
answers = []
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    set = {0}
    for j in range(n - 1):
        for k in range(j + 1, n):
            set.add(x[k] - x[j])
    answers.append(len(set) - 1)
for answer in answers:
    print(answer)