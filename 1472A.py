t = int(input())
answer = []
for i in range(t):
    n = list(map(int, input().split(" ")))
    count = 1
    while True:
        if n[0] % 2 == 0 or n[1] % 2 == 0:
            if n[0] % 2 == 0:
                count  *= 2
                n[0] = n[0] // 2
            if n[1] % 2 == 0:
                count *= 2
                n[1] = n[1] // 2
        else: break
    if count >= n [2]:
        answer.append("Yes")
    else:
        answer.append("No")
for i in range(t):
    print(answer[i])