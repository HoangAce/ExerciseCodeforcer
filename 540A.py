n = int(input())
n1 = list(map(int, input()))
n2 = list(map(int, input()))
step = 0
for i in range(n):
    step += min(abs(n1[i] - n2[i]), 10 - abs(n1[i] - n2[i]))
print(step)