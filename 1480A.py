t = int(input())
answers = []
for i in range(t):
    s = input()
    answer = ""
    for j in range(len(s)):
        if j % 2 == 0:
            if s[j] != 'a':
                answer += 'a'
            else:
                answer += 'b'
        else:
            if s[j] != 'z':
                answer += 'z'
            else:
                answer += 'y'
    answers.append(answer)
for answer in answers:
    print(answer)