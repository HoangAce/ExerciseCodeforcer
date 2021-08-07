def main():
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        c = input()
        for j in range(len(a)):
            if a[j] == b[j] != c[j] or b[j] != c[j] != a[j]:
                print("NO")
                break
        else:
            print("YES")


if __name__ == '__main__':
    main()
