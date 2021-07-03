t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    suma = sum(a) - n
    if suma >= 0:
        answers.append(suma)
    else:
        answers.append(1)
for answer in answers:
    print (answer)
