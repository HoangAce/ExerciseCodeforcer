t = int(input())
answer = []
for i in range(t):
    count = 0
    n = int(input())
    a = list(map(int, input().split(" ")))
    for j in a:
        if j > min(a):
            count += 1
    answer.append(count)
for i in answer:
    print(i)