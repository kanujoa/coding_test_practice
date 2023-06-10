# 한 국가의 등수 = 자신보다 더 잘한 나라 수 + 1
# 금, 은, 동메달 수가 모두 같으면 두 나라의 등수는 같음. (ex) 1등, 공동 2등, 4등 이런 식으로 나감)

n, k = map(int, input().split())     # 국가의 수, 등수를 알고 싶은 국가
medal = [list(map(int, input().split())) for _ in range(1, n+1)]     # 국가의 번호, 금, 은, 동메달 개수 순으로 입력
medal.sort(reverse=True, key=lambda x:(x[1], x[2], x[3]))     # 금메달 개수 기준으로 내림차순 정렬

rank = 0     # 현재 등수
cnt = 1     # 같은 메달이 나온 횟수
pre = []     # 바로 이전 나라의 메달 수
answer = []     # 등수를 담은 배열
for info in medal:
    if info[1:] == pre:
        answer.append([rank, info[0]])
        cnt += 1
    else:
        rank += cnt
        answer.append([rank, info[0]])
        cnt = 1
    pre = info[1:]
    if answer[-1][1] == k:
        print(answer[-1][0])
        break
