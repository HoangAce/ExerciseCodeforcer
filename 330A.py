def main():
    count = 0
    colum = []
    [r, c] = list(map(int, input().split()))
    for i in range(r):
        row = input()
        if row.find('S') == -1:
            count += 1
        else:
            for j in range(c):
                if row[j] == 'S':
                    colum.append(j)
    print(count * c + (c - len(set(colum))) * (r - count))
if __name__ == '__main__':
    main()