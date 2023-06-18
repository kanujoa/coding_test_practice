switch = int(input())     # 스위치 개수
state = list(map(int, input().split()))     # 스위치 상태
students = int(input())     # 학생 수
for _ in range(students):
    info = list(map(int, input().split()))     # [성별, 받은 숫자]
    if info[0] == 1:     # 남자라면
        for i in range(info[1]-1, len(state), info[1]):     # 자신이 받은 수의 배수 번호에 해당하는 스위치의 상태를 토글한다.
            if state[i] == 0:
                state[i] = 1
            else:
                state[i] = 0
    else:     # 여자라면 일단 해당하는 번호의 스위치 하나의 상태를 토글한다. 
        idx = info[1] - 1     # 여학생이 받은 번호
        if state[idx] == 0:    
            state[idx] = 1
        else:
            state[idx] = 0
        add = 1
        while True:
            if idx + add < len(state) and idx - add >= 0 and state[idx+add] == state[idx-add]:     # 현재 번호의 인덱스에 add를 더하거나 뺐을 때 마지막 인덱스와 0번 인덱스의 범위를 벗어나지 않고 현재 번호의 이전과 다음 스위치의 상태가 같을 때
                if state[idx-add] == 1:     # 현재 상태에서 토글한다.
                    state[idx-add] = state[idx+add] = 0
                else:
                    state[idx-add] = state[idx+add] = 1
                add += 1     
            else:
                break     # if문의 조건을 모두 만족하지 못하는 순간이 오면 반복문 종료

# 한 줄에 최대 20개씩만 출력하기
bind = 0
if switch % 20 == 0:
    bind = switch // 20
else:
    bind = switch // 20 + 1
for i in range(bind):
    print(' '.join(map(str, state[20*i : 20*(i+1)])))             