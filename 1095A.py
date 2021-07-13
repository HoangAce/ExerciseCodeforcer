n = int(input())
S = input()
count = 1
answerS = ""
count = 0
index = 0
while index < n:
    count += 1
    index += count
    answerS += S[index - 1]
print(answerS) 