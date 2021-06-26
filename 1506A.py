t = int(input())
answer = []
for i in range(t):
    numbers = list(map(int, input().split(" ")))
    if numbers[2] % numbers[0] == 0:
        answer.append((numbers[0] - 1) * numbers[1] + numbers[2] // numbers[0])
    else: 
        answer.append((numbers[2] % numbers[0] - 1) * numbers[1] + numbers[2] // numbers[0] + 1)
for i in answer:
    print(i)