def main():
    for i in range(int(input())):
        [n, k] = list(map(int, input().split()))
        if (n - 1)//2 < k:
            print(-1)
        else:
            for j in range(1, n + 1 - k):
                if(j <= k):
                    print(j, n + 1 - j, end=" ")
                else:
                    print(j, end=" ")
            print("")


if __name__ == '__main__':
    main()
