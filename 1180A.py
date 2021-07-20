def main():
    n = int(input())
    answer = 1
    for i in range(1, n):
        answer += i * 4
    print(answer)
if __name__ == '__main__':
    main()