w1 = input()
w2 = input()
w3 = ''
for i in range(0, len(w1)):
    if w1[i] == w2[i]:
        w3 += '0'
    else:
        w3 += '1'
print(w3)