t = int(input())
answer = []
for i in range(t):
    s = list(map(int, input().split(" ")))
    if s[0] > s[1]:
        a = s[0]
        b = s[1]
    else:
        a = s[1]
        b = s[0]
    count = 0
    while a <= s[2]:
        b += a
        tem = a
        a = b
        b = tem
        count += 1
    answer.append(count)
for i in answer:
    print(i)