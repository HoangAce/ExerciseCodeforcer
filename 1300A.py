def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count = a.count(0)
        if sum(a) + count == 0:
            count += 1
        print(count)
if __name__ == '__main__':
    main()
