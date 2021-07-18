count = 0
s = input()
t = input()
for i in t:
    if s[count] == i:
        count += 1
print(count + 1)