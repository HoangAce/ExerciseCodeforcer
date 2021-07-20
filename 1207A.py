def main():
    t = int(input())
    for i in range(t):
        [b, p, f] = list(map(int, input().split()))
        [h, c] = list(map(int, input().split()))
        if h >= c:
            if b // 2 >= p:
                print(p * h + min(b // 2 - p, f) * c)
            else:
                print(b // 2 * h)
        elif b // 2 >= f:
            print(f * c + min(b // 2 - f, p) * h)
        else:
            print(b // 2 * c)


if __name__ == '__main__':
    main()
