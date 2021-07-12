answers = []
t = int(input())
for i in range(t):
    n = int(input())
    if n <= 3:
        answers.append(n - 1)
    elif n % 2 == 0:
        answers.append(2)
    else:
        answers.append(3)
for answer in answers:
    print(answer)