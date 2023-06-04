n = int(input())
results = [input() for _ in range(n)]

for result in results:
    cnt = 0
    score = 0
    for i in range(len(result)):
        if result[i] == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)