def main():
    [a, b] = list(map(int, input().split()))
    if a == b:
        print(0, 6, 0)
    else:
        if (a + b) % 2 == 0:
            draw = 1
        else:
            draw = 0
        if a > b:
            print(6 - (a + b) // 2, draw, (a + b) // 2 - draw)
        else:
            print((a + b) // 2 - draw, draw, 6 - (a + b) // 2)


if __name__ == '__main__':
    main()
