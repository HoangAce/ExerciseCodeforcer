def main():
    for i in range(int(input())):
        P = int(input())
        if P % 2 == 0:
            print(2, P)
        else:
            print(2, P - 1)


if __name__ == '__main__':
    main()
