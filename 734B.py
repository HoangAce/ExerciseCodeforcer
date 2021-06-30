k = list(map(int, input().split()))
mink = min(k[0], k[2], k[3])
print(mink * 256 + 32 * min(k[1],k[0] - mink))