def main():
    t = int(input())
    for i in range(t):
        [n, x] = list(map(int, input().split()))
        w = list(map(int, input().split()))
        check = 0
        for j in range(n - 1):
            check += w[j]
            if check == x:
                w[j], w[j + 1] = w[j + 1], w[j]
                break
        if check + w[n - 1] == x:
            print("NO")
        else:
            print("YES")
            print(" ".join(map(str, w)))


if __name__ == '__main__':
    main()
