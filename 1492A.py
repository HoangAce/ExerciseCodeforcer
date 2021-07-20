def main():
    t = int(input())
    for i in range(t):
        [p, a, b, c] = list(map(int, input().split()))
        answer = []
        for i in [a, b, c]:
            if p % i == 0:
                answer.append(0)
                break
            if i > p:
                answer.append(i - p)
            else:
                answer.append(i * (p // i + 1) - p)
        print(min(answer))


if __name__ == '__main__':
    main()