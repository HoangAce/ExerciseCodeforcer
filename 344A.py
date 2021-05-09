n=int(input())
sum=0
w1=3
for i in range(0,n):
    w2=input()
    if w2!=w1:
        sum=sum+1
        w1=w2
    else:
        w1=w2
print(sum)