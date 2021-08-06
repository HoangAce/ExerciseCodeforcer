def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if min(a) < 0:
            print("NO")
        else:
            maxA = max(a) + 1
            print("YES")
            print(maxA)
            for j in range(maxA):
                print(j, end=" ")
            print("")


if __name__ == '__main__':
    main()
