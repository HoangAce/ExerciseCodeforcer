t = int(input())
answer = []
for i in range(t):
    s = list(map(int, input().split(" ")))
    if max(s[0], s[1]) < min(s[2],s[3]) or min(s[0], s[1]) > max(s[2],s[3]):
        answer.append("NO")
    else:
        answer.append("YES")
for i in answer:
    print(i)