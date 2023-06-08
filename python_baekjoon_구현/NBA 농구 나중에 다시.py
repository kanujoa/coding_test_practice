# 농구 경기는 48분동안, 각 팀이 몇 분동안 이기고 있는지를 출력하기
# 첫번째 줄에 1번 팀이 이기고 있던 시간, 둘째 줄에 2번 팀이 이기고 있던 시간 출력하기

def minutes_to_seconds(time):
    minutes, seconds = time.split(':')[0], time.split(':')[1]
    if minutes[0] == '0':
        minutes = minutes.replace('0', '', 1)
    if seconds[0] == '0':
        seconds = seconds.replace('0', '', 1)
    return [int(minutes), int(seconds)]

n = int(input())     # 골이 들어간 횟수
times = []
for _ in range(n):
    times.append(list(input().split()))     # 득점한 팀의 번호, 득점한 시간(분:초)

team_1_win = 0     # 1팀이 이긴 시간 기록(초로)
team_1_result = 0     # 1팀이 이기고 '있는' 시간 기록 (초로)
team_2_win = 0     # 2팀이 이긴 시간 기록(초로)
team_2_result = 0     # 2팀이 이기고 '있는' 시간 기록 (초로)

team = 0
for time in times:
    if time[0] == team:     # 연속으로 한 팀이 이겼을 경우
        team = time[0]

        minutes, seconds = minutes_to_seconds(time[1])

        if team == '1':
            team_1_result = minutes + seconds - team_1_win
            team_1_win = minutes + seconds
        elif team == '2':
            team_2_result = minutes + seconds - team_2_win
            team_2_win = minutes + seconds
    else:     # 바로 이전 득점 팀과 다른 팀이 이겼을 경우
        team = time[0]
        
        minutes, seconds = minutes_to_seconds(time[1])
        
        if team == '1':
            team_1_win = minutes + seconds
            team_2_result += team_1_win - team_2_win 
        elif team == '2':
            team_2_win = minutes + seconds
            team_1_result += team_2_win - team_1_win
        
print(team_1_result)
print(team_1_win)
print(team_2_result)
print(team_2_win)