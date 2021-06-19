n = int(input())
cards = [int(item) for item in input().split(" ")]
Sereja = 0
Dima =  0
for i in range(n):
    if i % 2 == 0:
        Sereja += max(cards[0], cards[-1])
    else:
        Dima += max(cards[0], cards[-1])
    cards.remove(max(cards[0], cards[-1]))
print(Sereja, Dima)

