from fractions import Fraction as F
n = list(map(int, input().split(" ")))
if max(n) == 1:
    print("1/1")
else: print(F(7 - max(n), 6))