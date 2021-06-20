n = input()
p = list(input().split(" "))
for item in p:
    if n[0] == item[0] or n[1] == item[1]:
        print("YES")
        break
else: print("NO")

