t = int(input())
p = []
for i in range(t):
    p.append(int(input()))
for i in p:
    if i % 2 == 0:
        for j in range(i,  0,  -1):
            print(j, end = " ")
    else:
        
        
        for j in range(i//2):
            print(j + i // 2 + 1, end = " ")
        print(i, end = " ")
        for j in range(i // 2, 0, -1):
            print(j, end = " ")
    print("")