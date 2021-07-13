def surplus(a):
    count = 0
    for num in a:
        count += int(num)
    if count % 4 == 0:
        return False
    return True
def main():
    a = int(input())
    while surplus(str(a)):
        a += 1
    print(a)
if __name__ == '__main__':
    main()
