t = int(input())
answer = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    count = 0
    min = a.index(1)
    for j in range(n - 1, -1, -1):
        if a[j] == 1:
            max = j
            break
    for book in a[min:max]:
        if book == 0:
            count += 1
    answer.append(count)
for step in answer:
    print(step)
