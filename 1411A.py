def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        for j in range(n - 1, -1, -1):
            if s[j] != ')':
                if(n - 1 - j) > (n // 2):
                    print('Yes')
                else:
                    print('No')
                break
        else:
            print('Yes')


if __name__ == '__main__':
    main()
