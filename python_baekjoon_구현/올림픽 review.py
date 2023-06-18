n, k = map(int, input().split())     # 국가의 수, 등수를 알고 싶은 국가

record = []
for _ in range(n):
    info = list(map(int, input().split()))     # 한줄씩 입력받기
    info.append(info.pop(0))     # info의 첫번째 요소는 국가를 나타내므로 맨 뒤로 보낸다.
    record.append(info)
record.sort(reverse=True)     # 금메달 수를 기준으로 내림차순(많은 것부터) 정렬 (금메달 수가 같을 경우 은메달, 동메달, 국가 번호 기준으로 차례로 기준을 움직이며 내림차순 정렬)

cnt = 1     # 동일한 기록을 가지고 있는 국가의 수 (자신 포함)
grade = 1     # 등수
for i in range(len(record)):     # 각 국가의 기록 하나씩 탐색
    if i == 0:     # 1등인 국가라면 (맨 앞에 위치한 국가)
        grade = 1     # 현재 등수 1로 수정
    else:     # 1등이 아닌 국가라면 
        if record[i][:3] == record[i-1][:3]:     # 앞선 국가와 기록이 동일하다면
            cnt += 1     # 동일 기록 국가 수 1 증가하고 등수는 변함 없이 그대로
        else:     # 앞선 국가와 기록이 다르다면
            grade += cnt     # 등수가 cnt만큼 건너뛰어야 함. (기록이 동일한 전적이 있다면 그만큼 아래로 감. 아닌 경우 그냥 등수 하나 아래로)
            cnt = 1     # cnt는 다시 1로 초기화
    if k == record[i][3]:     # 우리가 찾고자 하는 국가라면
        print(grade)      # 등수 출력
        break