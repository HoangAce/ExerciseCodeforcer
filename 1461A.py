def main():
    for i in range(int(input())):
        [n, k] = list(map(int, input().split()))
        if (n - k) % 3 == 2:
            print('a' * k + 'cba' * ((n - k) // 3) + 'cb')
        else:
            print('a' * k + 'cba' * ((n - k) // 3) + 'c' * ((n - k) % 3))


if __name__ == '__main__':
    main()
