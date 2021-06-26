t = int(input())
answer = []
for i in range(t):
    n = int(input())
    s = input()
    count = 0
    for num in s:
        if num == "0":
            count +=1
    if count >= n:
        answer.append("0" * n)
    else:
        answer.append("1" * n)
for string in answer:
    print(string)