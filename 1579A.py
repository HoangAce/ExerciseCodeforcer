def main():
    for i in range(int(input())):
        count = 0
        s = input()
        for j in s:
            if j == "B":
                count += 1
        if count == len(s) / 2:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
