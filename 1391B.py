t = int(input())
answers = []
for i in range(t):
    [n , m]= list(map(int, input().split()))
    grid = []
    for j in range(n):
        grid.append(input())
    count = 0
    for indexN in range(n - 1):
        if grid[indexN][m - 1] == "R":
            count += 1
    for indexM in range(m - 1):
        if grid[n - 1][indexM] == "D":
            count += 1
    answers.append(count)
for answer in answers:
    print(answer)