def main():
    [n, k] = list(map(int, input().split()))
    a = list(map(int, input().split()))
    setA = set(a)
    answer = []
    count = 0
    if len(setA) >= k:
        print("YES")
        for i in setA:
            if count < k:
                count += 1
                answer.append(a.index(i) + 1)
            else:
                break
        print(" ".join(map(str, sorted(answer))))
    else:
        print("NO")


if __name__ == '__main__':
    main()
