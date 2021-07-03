String = input()
len = len(String)
count = 0
for i in range(len):
    if String[i] == "Q":
        for j in range(i, len):
            if String[j] == "A":
                for k in range (j, len):
                    if String[k] == "Q":
                        count += 1
print (count)
