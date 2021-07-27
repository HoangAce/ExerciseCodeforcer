def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        count = 1
        sum = 1
        while sum < n:
            sum += count * 2 + 1
            count += 1
        print(count)
if __name__ == '__main__':
    main()