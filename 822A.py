def giaithua(number):
    if number == 1:
        return 1
    else: 
        return number * giaithua(number - 1)
a = list(map(int, input().split()))
print(giaithua(min(a)))

