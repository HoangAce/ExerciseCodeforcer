t = int(input())
answers = []
for i in range(t):
    n = int(input())
    b = input()
    num = "1"
    a ="1"
    for j in range(1, n):
        if b[j] == b[j - 1]:
            if num == "1":
                num = "0"
            else:
                num = "1"
        elif b[j] == "1":
            num = "1"
        a = a + num
    answers.append(a)
for answer in answers:
    print(answer)