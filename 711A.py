n = int(input())
seats = []
answer = "NO"
for i in range(n):
    row = input()
    if answer == "NO" and("OO" in row):
        answer = "YES"
        seats.append(row.replace("OO", "++", 1))
    else:
        seats.append(row)
print(answer)
if answer == "YES":
    for row in seats:
        print(row)

        
