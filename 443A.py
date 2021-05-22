n = (input()[1:-1]).split(", ")
setn = set(n)
if n[0] == "":
    print(0)
else:
    print(len(setn))