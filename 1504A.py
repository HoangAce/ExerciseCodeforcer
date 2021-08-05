def main():
    t = int(input())
    for i in range(t):
        s = input()
        lenS = len(s)
        for j in range(lenS):
            if s[j] != 'a':
                print('YES')
                print(s[0:(lenS - j)] + 'a' + s[(lenS - j):(lenS)])
                break
        else:
            print('NO')


if __name__ == '__main__':
    main()
