t = int(input())
answers = []
for i in range(t):
    numbers = list(map(int, input().split()))
    answers.append((numbers[0] - numbers[1]) * (numbers[2] // 2) + numbers[0] * (numbers[2] % 2))
for answer in answers:
    print(answer)