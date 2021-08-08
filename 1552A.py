def main():
    for i in range(int(input())):
        n = int(input())
        s = input()
        k = n
        sortS = sorted(s)
        for j in range(n):
            if s[j] == sortS[j]:
                k -= 1
        print(k)


if __name__ == '__main__':
    main()
