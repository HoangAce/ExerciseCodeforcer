def main():
    t = int(input())
    for i in range(t):
        s = [ord(c) for c in input()]
        lenS = len(s)
        a = 97
        count = 0
        for j in range(lenS):
            if s[j] == a:
                start = end = j
                count += 1
                break
        else:
            start = -1
        while start != -1:
            a = a + 1
            if start == 0:
                start = 1
            if end == lenS - 1:
                end = lenS - 2
            if a == s[start - 1]:                 
                start = start - 1
                count = count + 1
            elif a == s[end + 1]:
                end = end + 1
                count = count + 1
            else:
                start = -1
        if count == lenS:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
