t = int(input())
answer = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    indexMin = a.index(min(a))
    indexMax = a.index(max(a))
    count = 0
    if min(n - indexMin, indexMin + 1) <= min(n - indexMax, indexMax + 1):
        if n - indexMin >= indexMin + 1:
            answer.append(min(n - indexMin, indexMin + 1) + min(n - indexMax, indexMax - indexMin))
        else:
            answer.append(min(n - indexMin, indexMin + 1) + min(indexMin - indexMax, indexMax + 1))
    else:
        if n - indexMax >= indexMax + 1:
            answer.append(min(n - indexMax, indexMax + 1) + min(n - indexMin, indexMin - indexMax))
        else:
            answer.append(min(n - indexMax, indexMax + 1) + min(indexMax - indexMin, indexMin + 1))
for i in answer:
    print(i)