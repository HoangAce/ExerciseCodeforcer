def main():
    for i in range(int(input())):
        n = int(input())
        enemy = list(map(int, input()))
        Greor = list(map(int, input()))
        answer = 0
        for pawn in range(n):
            if Greor[pawn] == 1:
                if enemy[pawn] == 0:
                    answer += 1
                    enemy[pawn] = 2
                else:
                    if pawn != 0 and enemy[pawn - 1] == 1:
                        answer += 1
                    elif pawn != n - 1 and enemy[pawn + 1] == 1:
                        answer += 1
                        enemy[pawn + 1] = 2
        print(answer)


if __name__ == '__main__':
    main()
