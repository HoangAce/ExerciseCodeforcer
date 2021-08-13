def main():
    [n, k] = list(map(int, input().split()))
    a = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        if a[i] <= k:
            answer += 1
        else:
            break
    if answer < n:
        for i in range(n - 1, -1, -1):
            if a[i] <= k:
                answer += 1
            else:
                break
    print(answer)


if __name__ == '__main__':
    main()
