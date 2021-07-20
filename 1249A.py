def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        a = sorted(map(int, input().split()))
        for j in range(n - 1):
            if a[j + 1] - a[j] == 1:
                print(2)
                break
        else:
            print(1)
if __name__ == '__main__':
    main()