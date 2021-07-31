def main():
    t = int(input())
    for i in range(t):
        [n, k1, k2] = list(map(int, input().split()))
        [w, b] = list(map(int, input().split()))
        if (k1 + k2) >= 2 * w and (2 * n - k1 - k2) >= 2 * b:
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    main()
