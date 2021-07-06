t = int(input())
answers = []
for i in range(t):
    S = input()
    count = 0
    count1 = []
    for number in S:
        if number == "1":
            count += 1
        elif count > 0:
            count1.append(count)
            count = 0
    else: count1.append(count)
    answers.append(count1)
for answer in answers:
    answer.sort(reverse=True)
    count = 0
    for i in range(len(answer)):
        if i % 2 == 0:
            count += answer[i]
    print(count)