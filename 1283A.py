t = int(input())
minutes = []
for i in range(t):
    time = list(map(int, input().split(" ")))
    minutes.append((24 - time[0])* 60 - time[1])
for minute in minutes:
    print(minute)