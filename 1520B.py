t = int(input())
answer = []
for i in range(t):
    n = input()
    if int(n) < int(n[0] * len(n)):
        answer.append(int(n[0]) - 1 + (len(n) - 1) * 9)
    else:
        answer.append(int(n[0]) + (len(n) - 1) * 9)
for i in answer:
    print(i)