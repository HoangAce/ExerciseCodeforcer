def main():
    t = int(input())
    for i in range(t):
        [x, y] = (lambda arr: [max(arr), min(arr)])(list(map(int, input().split())))
        print(2 * x - (0 if(x == y) else 1))
if __name__ == '__main__':
    main()