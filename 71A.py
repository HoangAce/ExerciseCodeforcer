n = int(input())
words = list()
for t in range(0,n):
    words.append(input())
 
for word in words:
    if(len(word) <= 10):
        print(word)
    else:
        print(word[0] + str(len(word)-2) + word[-1])