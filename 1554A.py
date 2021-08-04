def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        Max = 0
        for i in range(n - 1):
            if a[i] * a[i + 1] > Max:
                Max = a[i] * a[i + 1]
        print(Max)


if __name__ == '__main__':
    main()
