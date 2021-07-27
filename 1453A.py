def main():
    t = int(input())
    for i in range(t):
        count = 0
        [n, m] = list(map(int, input().split()))
        ArrN = list(map(int, input().split()))
        ArrM = list(map(int, input().split()))
        if n < m:
            for N in ArrN:
                if N in ArrM:
                    count += 1
        else:
            for M in ArrM:
                if M in ArrN:
                    count += 1
        print(count)
if __name__ == '__main__':
    main()