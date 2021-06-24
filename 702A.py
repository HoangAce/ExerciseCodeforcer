n = int(input())
arr = list(map(int, input().split(" ")))
maxLen = 1
count = 1
for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        count += 1
    else:
        count = 1
    if count > maxLen:
        maxLen = count
print(maxLen)
        
