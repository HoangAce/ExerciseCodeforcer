t = int(input())
answers =  []
for i in range(t):
    n = int(input())
    a = set(map(int, input().split(" ")))
    answers.append(len(a))
for answer in answers:
    print(answer)