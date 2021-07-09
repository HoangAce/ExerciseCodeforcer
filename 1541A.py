t = int(input())
numCat = []
for i in range(t):
    numCat.append(int(input()))
for cats in numCat:
    if cats % 2 == 0:
        for cat in range(0, cats, 2):
            print(cat + 2, cat + 1, end = " ")
        print("")
    else:
        for cat in range(0, cats - 3, 2):
            print(cat + 2, cat + 1, end = " ")
        print(cats, cats -2, cats - 1)
