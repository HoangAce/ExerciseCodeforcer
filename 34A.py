import math


def main():
    n = int(input())
    a = list(map(int, input().split()))
    min = abs(a[0] - a[n - 1])
    x = 1
    y = n
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) < min:
            min = abs(a[i] - a[i + 1])
            x = i + 1
            y = i + 2
    print(x, y)


if __name__ == '__main__':
    main()
