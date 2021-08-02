def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(n // 10 + (n % 10) // 9)


if __name__ == '__main__':
    main()
