def main():
    [n, c] = list(map(int, input().split()))
    t = list(map(int, input().split()))
    number = 1
    for i in range(1, n):
        if t[i] - t[i - 1] <= c:
            number += 1
        else:
            number = 1
    print(number)
if __name__ == '__main__':
    main()
