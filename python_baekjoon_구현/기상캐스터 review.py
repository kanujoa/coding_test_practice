h, w = map(int, input().split())     # 행의 수, 열의 수
state = [list(item for item in input()) for _ in range(h)]     # 입력으로 주어지는 구름의 상태 (공백이 없이 주어진다.)
answer = [[-2] * w for _ in range(h)]

passed_time = 0     # 지나간 시간(분)
while True:
    for i in range(h):     # i: 행
        for j in range(w):     # w: 열
            if state[i][j] == 'c' and answer[i][j] == -2:     # 해당 자리에 구름이 있고 이전에 구름이 지나간 적이 없는 자리라면
                answer[i][j] = passed_time     # answer의 해당 자리에 지나간 시간을 기록해 줌.
        # 하나의 행이 끝나면 그 행에서의 구름을 오른쪽(동쪽)으로 한칸씩 이동해줌. 외부에서 구름이 들어오는 경우는 없기 때문에 새로 들어오는 것은 '.'이다.
        state[i].pop()
        state[i].insert(0, '.')
    passed_time += 1     # 모두 한칸씩 이동이 끝나면 지나간 시간도 1 추가해줌.
    for s in state:      # state에 더 이상 구름이 없는지 확인
        if 'c' in s:     # 아직 구름이 남아 있다면
            break     # 멈추고 다시 while문으로 돌아가기
    else:     # 구름이 남아 있지 않은 경우
        for i in range(h):
            for j in range(w):
                if answer[i][j] == -2:     # answer에 남아 있는 -2인 부분을
                    answer[i][j] = -1     # -1로 바꿈.
        break     # 그 후 while문 종료
    
for item in answer:
    print(' '.join(map(str, item)))