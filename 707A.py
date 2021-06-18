t = list(map(int, input().split(" ")))
a = []
color = ['C', 'M', 'Y']
for i in range(t[0]):
    a  += list(input().split(" "))
for i in a:
    if i in color:
        print("#Color")
        break
else: print("#Black&White")
            