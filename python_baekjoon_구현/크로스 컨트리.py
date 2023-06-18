# 4번째 주자에서 구해지지 않을 시 5번째 주자 1번만 구하고 끝내면 된다.
# 실패...

# T = int(input())     # 테스트 케이스의 개수

# for _ in range(T):
#     people = int(input())
#     order = list(map(int, input().split()))

#     scores = {}
#     score = 1
#     for team in order:
#         if team not in scores:
#             if order.count(team) >= 6:
#                 scores[team] = [score]
#                 score += 1
#             else:
#                 scores[team] = 'n/a'
#         else:
#             if scores[team] != 'n/a':
#                 scores[team].append(score)
#                 score += 1
    
#     score_sum = {}
#     for team in scores:
#         if scores[team] != 'n/a':
#             if team not in score_sum:
#                 score_sum[team] = sum(scores[team][:4])

#     values = list(score_sum.values())
#     if values.count(min(values)) == 1:
#         _min = values.index(min(values))
#         print(list(score_sum.keys())[_min])
#     else:
#         for team in scores:
#             if scores[team] != 'n/a':
#                 score_sum[team] += scores[team][4]
#         values = list(score_sum.values())
#         _min = values.index(min(values))
#         print(list(score_sum.keys())[_min])


# 다른 사람의 코드

t = int(input())

for _ in range(t):
    n = int(input())
    count = {}     # 팀 당 주자 수
    temp = list(map(int, input().split()))     # 도착한 팀 순서 입력받기

    # 팀 별로 주자 수 세기 
    for i in range(n):
        if temp[i] in count:     # count dic에 해당 팀 이름이 key로 있으면     
            count[temp[i]] += 1     # 그 값에 1 추가
        else:     # 그렇지 않으면 
            count[temp[i]] = 1      # 팀 이름을 key로 새로 생성하고 값을 1로 함.
    
    # 제외되는 팀 구하기
    dele = {}     
    for k, v in count.items():     # count dic의 key가 k로, value가 v로 할당됨.
        if v < 6:     # 6명이 되지 않는 팀은
            dele[k] = 1      # dele dic의 key로 추가됨. (값은 임의로 1)
    
    # 점수 계산
    team = {}
    idx = 1     # 점수
    for i in range(n):     # 선수 수만큼 반복
        if temp[i] not in dele:     # 해당 팀이 dele dic에 있으면
            if temp[i] in team:     # 해당 팀이 team dic에 key로 존재한다면
                if team[temp[i]][0] < 4:      # 그 팀의 cnt가(0번 요소) 4보다 작다면
                    team[temp[i]][0] += 1     # 그 팀의 cnt 증가
                    team[temp[i]][1] += idx      # 그 팀의 점수(1번 요소) 증가
                elif team[temp[i]][0] == 4:     # 그 팀의 cnt가 4라면
                    team[temp[i]][0] += 1     # 그 팀의 cnt 증가
                    team[temp[i]][2] = idx      # 5번째 주자의 점수(2번 요소)가 현재 점수가 됨.
        else:     # 해당 팀이 dele dic에 없으면
            team[temp[i]] = [1, idx, 0]     # [팀당 주자 수, 상위 4명 점수 합, 5번째 주자의 점수]

        idx += 1

    # 순위 정렬
    team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))