# 무승부와 패배를 같이 진행하면 안된다! 무승부 3번이면 패배 2번 이런 식으로 살펴보아야 한다. (둘 중에 하나만 살펴야!)

answer = []

for _ in range(4):
    results = list(map(int, input().split()))     # 승, 무, 패 결과 입력받아 1차원 리스트에 담기
    team_results = [[results[i], results[i+1], results[i+2]] for i in range(0, len(results), 3)]     # results를 가공하여 팀별로 [승, 무, 패] 결과 저장 (2차원 리스트)
    team_results.sort(reverse=True)     # 승이 많은 팀부터 내림차순 정렬 (승이 같으면 무승부, 무승부가 같으면 패가 많은 팀 기준으로 내림차순 정렬)

    # 승, 무, 패의 합이 5가 되지 않는지를 확인
    for results in team_results:
        if results[0] + results[1] + results[2] != 5:
            answer.append(0)
            break
    else:
        for i in range(len(team_results)):
            cnt = 0     # 패배와 성공을 매칭할때의 cnt

            # 패배가 많은 것부터 승리와 매칭해야 하기 때문에 team_results를 거꾸로 진행한다.
            for j in range(len(team_results)-1, -1, -1):
                win = team_results[i][0]     # 현재 팀의 승리 수
                draw = team_results[i][1]     # 현재 팀의 무승부 수
                lose = team_results[i][2]     # 현재 팀의 패배 수
                if j != i:     # 현재 팀에 해당하지 않을 경우
                    other_draw = team_results[j][1]     # 다른 팀의 무승부 수
                    other_lose = team_results[j][2]     # 다른 팀의 패배 수
                    if win > 0 and other_lose > 0 and cnt != win:     # 현재 팀의 승리 수가 0보다 클 경우    
                        team_results[j][2] -= 1     # 다른 팀의 패배 부분과 짝지어지므로 -1하기
                        cnt += 1
                    elif draw > 0 and other_draw > 0:     # 현재 팀의 무승부 수와 다른 팀의 무승부 수 모두 남아 있을 경우
                        team_results[i][1] -= 1
                        team_results[j][1] -= 1     # 서로 짝지어질 수 있으므로 두 팀의 무승부 부분 1씩 감소
        else:      # break 없이 통과하면
            # 위의 코드로 인해 변형된 team_result에서 무승부와 패배 부분의 합이 0이 되지 않으면 불가능한 결과이다.
            draw_sum = 0
            lose_sum = 0
            for result in team_results:
                draw_sum += result[1]
                lose_sum += result[2]
                if draw_sum != 0 or lose_sum != 0:
                    answer.append(0)
                    break
            else:
                answer.append(1)

for item in answer:
    print(item, end=' ')                     