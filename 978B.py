n = int(input())
string = input()
answer = 0
i = 0
while (i < n) :
    if string[i] == "x":
        count = 0
        for char in string[i:]:
            if char == "x":
                count += 1
            else:
                break
        i = i + count + 1
        if count > 2:
            answer += count - 2
    else:
        i += 1
print(answer)

