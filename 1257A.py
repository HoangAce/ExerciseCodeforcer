def main():
    t = int(input())
    for i in range(t):
        [n, x, a, b] = list(map(int, input().split()))
        print(min(n - 1, abs(a - b) + x))


if __name__ == '__main__':
    main()
