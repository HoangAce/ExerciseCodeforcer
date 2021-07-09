t = int(input())
answers = []
for i in range(t):
    numbers = list(map(int, input().split()))
    if (numbers[1] - numbers[0]) % (numbers[2] + numbers[3]) == 0:
        answers.append((numbers[1] - numbers[0]) // (numbers[2] + numbers[3]))
    else:
        answers.append(-1)
for answer in answers:
    print(answer)