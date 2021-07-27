def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        check = n % 3
        answer = n // 3
        if check == 1:
            print(answer + 1,answer)
        elif check == 2:
            print(answer, answer + 1)
        else:
            print(answer, answer)
if __name__ == '__main__':
    main()