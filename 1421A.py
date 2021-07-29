def main():
    t = int(input())
    for i in range(t):
        [a, b] = list(map(int, input().split()))
        print(a + b - 2 * (a & b))
if __name__ == '__main__':
    main()
