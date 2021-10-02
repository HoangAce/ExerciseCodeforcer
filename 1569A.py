import math


def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        for j in range(n - 1):
            if s[j] != s[j + 1]:
                print(j + 1, j + 2)
                break
        else:
            print(-1, -1)


if __name__ == '__main__':
    main()
