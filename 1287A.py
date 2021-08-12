def main():
    for i in range(int(input())):
        k = int(input())
        s = input()
        max = 0
        count = 0
        check = False
        for student in s:
            if student == 'A':
                if count > max:
                    max = count
                count = 0
                check = True
            elif check == True:
                count += 1
        if s[-1] == 'P' and count > max:
            max = count
        print(max)


if __name__ == '__main__':
    main()
