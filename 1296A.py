t = int(input())
answers = []
for i in range(t):
    n = int(input())
    a = list(map(lambda x: int(x) % 2, input().split(" ") ))
    if 1 not in a:
        answers.append("NO")
    elif 0 not in a and n % 2 == 0:
        answers.append("NO")
    else:
        answers.append("YES")
for answe in answers:
    print(answe)
