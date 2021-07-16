t = int(input())
for i in range(t):
    fuck = input()
    [xA, yA] = list(map(int, input().split()))
    [xB, yB] = list(map(int, input().split()))
    [xF, yF] = list(map(int, input().split()))
    if xA == xB == xF and (abs(yA - yF) + abs(yF - yB)) == abs(yA - yB) or yA == yB == yF and (abs(xA - xF) + abs(xF - xB)) == abs(xA - xB):
        print(abs(xA - xB + yA - yB) + 2)
    else:
        print(abs(xA - xB) + abs(yA - yB))