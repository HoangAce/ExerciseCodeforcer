n = int(input())
answer = 0
x = 1
def dequy(x):
    if x == 1:
        return 1
    return x + dequy(x - 1)
while True:
    answer += dequy(x)
    if answer > n:
        print(x - 1)
        break
    x += 1
