t = int(input())
answer = []
for i in range(t):
    numbers = list(map(int, input().split(" ")))
    if numbers[0] == numbers[1]:
        answer.append(0)
    elif numbers[0] > numbers[1]:
        if (numbers[0] - numbers[1]) % 2 == 1:
            answer.append(2)
        else:
            answer.append(1)
    else:
        if (numbers[0] - numbers[1]) % 2 == 1:
            answer.append(1)
        else:
            answer.append(2)
for i in answer:
    print(i)