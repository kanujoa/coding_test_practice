p = int(input())     # 테스트 케이스의 개수
for _ in range(p):
    row = []     # 학생들을 줄세우기 위한 리스트 (아래의 코드로 인해 항상 오름차순 유지)
    cnt = 0     # 학생들이 물러난 걸음의 수
    info = list(map(int, input().split()))     # 테스트 케이스 번호와 학생들의 키 입력받기
    case_num = info[0]     # 테스트 케이스 번호
    height = info[1:]     # 학생들의 키 리스트

    for h in height:
        if len(row) == 0:     # 줄이 비어 있으면
            row.append(h)      # 그냥 그 학생 추가
        else:     # 줄이 비어 있지 않다면
            if h >= row[-1]:     # 현재 학생의 키가 맨 뒤에 서있는 학생(지금까지 row에서 가장 키가 큰 학생)의 키보다 크거나 같다면
                row.append(h)      # 그냥 맨 뒤에 서고 끝내기 (물러서기 없음.)
            else:      # 현재 학생의 키가 맨 뒤에 서있는 학생보다 작다면
                for i in range(len(row)):
                    if row[i] > h:     # row에 있는 학생들의 키를 0번 인덱스부터 살펴 처음으로 h보다 큰 학생이 나오면
                        cnt += len(row) - i     # i번 자리 학생부터 한 걸음씩 뒤로 물러나고 그 걸음 수를 기록
                        row.insert(i, h)     # 그 자리에 h 삽입
                        break     # 삽입한 이후에는 break로 반복문을 종료해야 한다.
    
    print(case_num, cnt)     # 테스트 케이스 번호와 물러난 걸음 수를 공백을 두고 함께 출력