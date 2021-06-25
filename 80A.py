def is_prime_basic(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True
numbers = list(map(int, input().split(" ")))
if is_prime_basic(numbers[1]):
    for num in range(numbers[0] + 1,numbers[1]):
        if is_prime_basic(num):
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")