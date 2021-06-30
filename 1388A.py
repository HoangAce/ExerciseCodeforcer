t = int(input())
numbers = []
for i in range(t):
    numbers.append(int(input()))
for number in numbers:
    if number > 30:
        print("YES")
        if number % 2 == 0 and number != 46:
            print(6,10,15,number - 6 - 10 - 15)
        else:
            print(6,10,14,number - 6 - 10 - 14)
    else:
        print("NO")