t = int(input())
answers = []
for i in range(t):
    S = input()
    count = 0
    begin = 0
    end = 0
    while True:
        begin = S.find("10",end)
        end = S.find("01",begin)
        if begin != -1 and end != -1:
            count += end - begin
        else:
            break
    answers.append(count)
for answer in answers:
    print(answer)