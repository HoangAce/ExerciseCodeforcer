def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n - 1, -1, -1):
        if a[i] not in b:
            b.append(a[i])
    lenB = len(b)
    print(lenB)
    for i in range(lenB - 1, -1, -1):
        print(b[i], end=" ")
    print("")


if __name__ == '__main__':
    main()
