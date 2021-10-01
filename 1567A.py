def main():
    for i in range(int(input())):
        n = int(input())
        answer = ""
        for j in input():
            if j == "U":
                answer += "D"
            elif j == "D":
                answer += "U"
            else:
                answer += j
        print(answer)


if __name__ == '__main__':
    main()
