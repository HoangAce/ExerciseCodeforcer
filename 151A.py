a  = list(map(int, input().split(" ")))
print(min(a[1]*a[2]//a[6], a[3]*a[4], a[5]//a[7])//a[0])