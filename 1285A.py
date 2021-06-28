n = int(input())
S = input()
left = 0
right = 0
for i in S:
    if i == "L":
        left -= 1
    else: right += 1
print(right - left + 1)