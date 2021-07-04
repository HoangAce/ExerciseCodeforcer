t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    for num in a:
        count = a.count(num)
        if count > max:
            max = count
    answers.append(max)
for answer in answers:
    print(answer)