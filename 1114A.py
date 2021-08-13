def main():
    [x, y, z] = list(map(int, input().split()))
    [a, b, c] = list(map(int, input().split()))
    if (a >= x):
        if(a - x + b >= y):
            if(a + b + c >= x + y + z):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')


if __name__ == '__main__':
    main()
