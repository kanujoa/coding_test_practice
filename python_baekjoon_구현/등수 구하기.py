n, new_score, p = map(int, input().split())
if n == 0:
    print(1)
    exit()
scores = list(map(int, input().split()))
if new_score > min(scores) and len(scores) == p:
    scores.append(new_score)
    scores.pop(scores.index(min(scores)))
elif new_score <= min(scores) and len(scores) == p:
    print(-1)
    exit()
else:
    scores.append(new_score)
scores.sort(reverse=True)
rank = 0
pre = -1
cnt = 0
for i in range(len(scores)):
    if pre != scores[i]:
        rank += 1
        rank += cnt
        cnt = 0     # 같은 숫자가 더 나온 횟수를 나타내는 cnt 초기화를 잊지 말자
    else:
        cnt += 1
    if scores[i] == new_score:
        print(rank)
        break
    else:
        pre = scores[i]