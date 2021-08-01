def main():
    q = int(input())
    for i in range(q):
        [l1, r1, l2, r2] = list(map(int, input().split()))
        if r1 == l2:
            print(l1, r2)
        else:
            print(r1, l2)
if __name__ == '__main__':
    main()
