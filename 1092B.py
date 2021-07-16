n = int(input())
a = sorted(list(map(int, input().split())))
answer = 0
for i in range(n // 2):
    answer += a[2 * i + 1] - a[2 * i]
print(answer)