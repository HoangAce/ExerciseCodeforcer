def main():
    t = int(input())
    for i in range(t):
        s = sorted(input())
        count = 1
        answer = 0
        duplicate = False
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                if duplicate == False:
                    duplicate = True
                    count -= 1
                    answer += 1
            else:
                duplicate = False
                count += 1
        print(answer + count // 2)
if __name__ == '__main__':
    main()
