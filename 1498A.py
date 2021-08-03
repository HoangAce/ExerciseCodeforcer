def gcdSum(x):
    y = 0
    for char in str(x):
        y += int(char)
    while y > 0:
        temp = x
        x = y
        y = temp % y
    return x


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        while gcdSum(n) == 1:
            n += 1
        print(n)


if __name__ == '__main__':
    main()
