answers = []
t = int(input())
for i in range(t):
    n = int(input())
    if n % 2050 != 0:
        answers.append(-1)
    else:
        temp = n // 2050
        count = 0
        while temp != 0:
            count += temp % 10
            temp = temp // 10
        answers.append(count)
for answer in answers:
    print(answer)