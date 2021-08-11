def main():
    [n, q] = list(map(int, input().split()))
    s = input()
    a = [0]
    for i in range(n):
        a.append(a[-1] + ord(s[i]) - 96)
    for i in range(q):
        [l, r] = list(map(int, input().split()))
        print(a[r] - a[l - 1])


if __name__ == '__main__':
    main()
