import math


def main():
    for i in range(int(input())):
        k = int(input())
        answer1 = math.ceil(math.sqrt(k))
        answer2 = pow(answer1, 2) + 1 - k
        if answer1 >= answer2:
            print(answer1, answer2)
        else:
            print(2 * answer1 - answer2, answer1)


if __name__ == '__main__':
    main()
