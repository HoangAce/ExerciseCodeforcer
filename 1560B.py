def main():
    for i in range(int(input())):
        [a, b, c] = list(map(int, input().split()))
        if max(a, b, c) > abs(a - b) * 2:
            print(-1)
        elif c > abs(a - b):
            print(c - abs(a - b))
        else:
            print(abs(a - b) + c)


if __name__ == '__main__':
    main()
