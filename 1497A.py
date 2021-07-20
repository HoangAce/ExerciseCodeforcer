def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        j = 0
        count = n - 1
        while j < count:
            if a[j] == a[j + 1]:
                for k in range(j + 1, count):
                    a[k] = a[k + 1]
                a[count] = a[j]
                count -= 1
            else:
                j += 1
        print(" ".join(map(str,a)))
if __name__ == '__main__':
    main()