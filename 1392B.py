def main():
    for i in range(int(input())):
        [n, k] = list(map(int, input().split()))
        a = list(map(int, input().split()))
        if k % 2 == 0:
            minA = min(a)
            for j in range(n):
                print(a[j] - minA, end=" ")
        else:
            maxA = max(a)
            for j in range(n):
                print(maxA - a[j], end=" ")
        print("")


if __name__ == '__main__':
    main()
