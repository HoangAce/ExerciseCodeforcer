
def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)
index = 0
numbers = [int(item) for item in list(input().split(" "))]
while numbers[2] >= 0:
    if (index == 0):
        numbers[2] -= gcd(numbers[0], numbers[2])
        index = 1
    elif (index == 1):
        numbers[2] -= gcd(numbers[1], numbers[2])
        index = 0
print(index)