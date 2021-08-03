def main():
    n = int(input())
    a = list(map(int, input().split()))
    answer = []
    amount = 1
    count = 1
    for i in range(1, n):
        if a[i] == 1:
            answer.append(count)
            amount += 1
            count = 1
        else:
            count += 1
    answer.append(count)
    print(amount)
    print(' '.join(map(str, answer)))


if __name__ == '__main__':
    main()
