t = int(input())
answer = []
for i in range(t):
    a  = list(map(int, input().split(" ")))
    sum  = a[0] + a[1] + a[2] + a[3]
    if sum % 3 == 0 and (sum / 3) >= max(a[0:3]) :
        answer.append("YES")
    else:
        answer.append("NO")
for i in answer:
    print(i)