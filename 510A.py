# -*- coding: utf- 8-*-
t = input().split(" ")
n = int(t[0])
m = int(t[1])
for i in range(n):
    if i % 2 ==0:
        print('#' * m)
    elif ((i - 1) / 2) % 2 == 0:
        print('.' * (m - 1) + '#')
    else:
        print('#' + '.' * (m - 1))