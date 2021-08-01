def main():
    a = list(map(int, input().split()))
    if (max(a) == sum(a) / 2) or ((max(a) + min(a) == sum(a) / 2)):
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':
    main()
