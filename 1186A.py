name = input()
count = min(abs(ord(name[0]) -  ord('a')), 26 - abs(ord(name[0]) -  ord('a')))
for i in range(len(name) - 1):
    count += min(abs(ord(name[i + 1]) -  ord(name[i])), 26 - abs(ord(name[i + 1]) -  ord(name[i])))
print(count)