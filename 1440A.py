def main():
    t = int(input())
    for i in range(t):
        [n, c0, c1, h] = list(map(int, input().split()))
        count = 0
        for char in input():
            if char == "1":
                count += 1
        print(count * min(c1, c0 + h) + (n - count) * min(c0, c1 + h))


if __name__ == '__main__':
    main()
