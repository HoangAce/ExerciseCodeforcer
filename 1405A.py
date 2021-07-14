def main():
    answers = []
    t = int(input())
    for i in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        p.reverse()
        answers.append(p)
    for answer in answers:
        print(" ".join(map(str, answer)))
if __name__ == '__main__':
    main()