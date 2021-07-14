def main():
    answers = []
    t = int(input())
    for i in range(t):
        [n, m] = list(map(int, input().split()))
        a = list(map(int, input().split()))
        if sum(a) == m:
            answers.append("YES")
        else:
            answers.append("NO")
    for answer in answers:
        print(answer)
if __name__ == '__main__':
    main()