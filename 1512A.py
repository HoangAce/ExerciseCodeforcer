t = int(input())
answer = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    index1 = a.index(a[0])
    count1 = 1
    count2 = 0
    for j in range(1, n):
        if index1 == a.index(a[j]):
            count1 += 1
        else:
            index2 = a.index(a[j])
            count2 += 1
        if count1 > 1 and count2 == 1:
            answer.append(index2 + 1)
            break
        if count2 > 1 and count1 == 1:
            answer.append(index1 + 1)
            break
for i in answer:
    print(i)