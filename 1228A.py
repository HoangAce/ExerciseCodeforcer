def check(x):
    for i in range(10):
        if str(x).count(str(i)) > 1:
            return False
    else:
        return True
def main():
    [l, r] = list(map(int, input().split()))
    for i in range(l, r + 1):
        if check(i):
            print(i)
            break
    else:
        print(-1)
if __name__ == '__main__':
    main()
