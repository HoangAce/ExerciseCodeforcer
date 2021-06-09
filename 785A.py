n = int(input())
sum = 0
for item in range(0 , n):
    poly = input()
    if poly == "Tetrahedron":
        sum += 4
    elif poly == "Cube":
        sum += 6
    elif poly == "Octahedron":
        sum += 8
    elif poly == "Dodecahedron":
        sum += 12
    else:
        sum += 20
print(sum)
