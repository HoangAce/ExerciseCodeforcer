def main():
    for i in range(int(input())):
        k = int(input())
        i = 1
        num = 1
        while i < k or num % 3 == 0 or num % 10 == 3:
            if num % 3 == 0 or num % 10 == 3:
                num += 1
            else:
                i += 1
                num += 1
        print(num)


if __name__ == '__main__':
    main()
