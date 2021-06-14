#-*- coding: utf- 8-*-
n = int(input())
answer = 0
for i in range(n):
    a = list(map(int, input().split(" ")))
    if(a[0] > a[1]):
        answer += 1
    elif(a[0] < a[1]):
        answer -= 1
if (answer > 0):
    print("Mishka")
elif (answer < 0):
    print("Chris")
else: print("Friendship is magic!^^")