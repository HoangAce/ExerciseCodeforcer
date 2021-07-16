t = int(input())
for i in range(t):
    answer = 1
    count = 1
    n = int(input())
    x = list(map(int, input().split()))
    for j in range(1, n):
        if x[j] == x[j - 1]:
            count += 1
        elif x[j] - x[j - 1] == 1:
            answer += 1
        elif count > 1:
            answer += 2
            count = 1
        else:
            answer += 1
            count = 1
    if count > 1:
        answer += 1
    print(answer)