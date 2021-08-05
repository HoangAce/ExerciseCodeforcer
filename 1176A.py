def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        count = 0
        while n % 2 == 0:
            count += 1
            n = n//2
        while n % 3 == 0:
            count += 2
            n = n//3
        while n % 5 == 0:
            count += 3
            n = n//5
        if n == 1:
            print(count)
        else:
            print(-1)


if __name__ == '__main__':
    main()
