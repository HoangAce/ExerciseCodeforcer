n = int(input())
str = input()
one = 0
zero = 0
for char in str:
    if char == "n":
        one += 1
    elif char == "z":
        zero += 1
print("1 " * one + "0 " *zero)

