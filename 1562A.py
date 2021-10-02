import math


def main():
    for i in range(int(input())):
        [l, r] = list(map(int, input().split()))
        if 2 * l > r:
            print(r - l)
        else:
            print(math.ceil(r / 2) - 1)


if __name__ == '__main__':
    main()
