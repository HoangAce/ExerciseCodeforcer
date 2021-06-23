string = input()
i = 0
num = ""
while i < len(string):
    if string[i] == ".":
        num += "0"
        i += 1
    elif string[i] == "-":
        if string[i + 1] == ".":
            num += "1"
        else:
            num += "2"
        i +=2
print (num)