t = int(input())
coordinates = []
for i in range(t):
    row1 = -1
    row2 = -1
    colum1 = -1
    colum2 = -1
    n = int(input())
    for j in range(n):
        row = input()
        if row2 == -1:
            for k in range(n):
                if row[k] == '*':
                    if row1 == -1:
                        row1 = j
                    else:
                        row2 = j
                    if colum1 == -1:
                        colum1 = k
                    else:
                        colum2 = k
    coordinates.append([n, row1, row2, colum1, colum2])
for [n, row1, row2, colum1, colum2] in coordinates:
    if row1 == row2:
        minColum = min(colum1, colum2)
        maxColum = max(colum1, colum2)
        if (row1 + row1 + 2) == (n + 1):
            row2 = row1 + 1
        else: row2 = n - 1 - row1
    elif  colum1 == colum2:
        minColum = min(colum1, n - 1 - colum1)
        maxColum = max(colum1, n - 1 - colum1)
        if minColum == maxColum:
            maxColum = minColum + 1
    else:
        minColum = min(colum1, colum2)
        maxColum = max(colum1, colum2)
    for j in range(n):
        if j == row1 or j == row2:
            print('.' * minColum + '*' + '.' * (maxColum - minColum - 1 ) + '*' + '.' * (n - maxColum  - 1))
        else:
            print('.' * n )