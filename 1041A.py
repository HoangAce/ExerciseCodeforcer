def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) + 1 - min(a) - n)
if __name__ == '__main__':
    main()
