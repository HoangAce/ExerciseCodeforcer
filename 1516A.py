t = int(input())
for i in range(t):
    [n, k] = list(map(int,input().split()))
    a = list(map(int,input().split()))
    index = 0
    while k > 0:
        if a[index] == 0:
            index += 1
            if index == n - 1:
                break
        else:
            a[index] -= 1
            a[n - 1] += 1
            k -= 1
        
    print(" ".join(map(str, a)))