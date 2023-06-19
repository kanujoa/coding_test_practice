n = int(input())     # 사람의 수
taller = list(map(int, input().split()))     # 자신보다 키가 더 큰 사람의 수를 입력받아 리스트로 만들기
for i in range(len(taller)):
    taller[i] = [taller[i], i + 1]     # taller의 각 요소들(사람들)을 자신보다 더 큰 사람의 수와 키룰 묶은 리스트로 변경
taller.sort(key=lambda x:(x[0], -x[1]))     # 자신보다 더 큰 사람의 수가 적은 것부터 시작하도록 정렬, 더 큰 사람의 수가 같다면 키 내림차순으로 정렬 (큰게 먼저 와야지 작은 것이 그것과 비교하여 위치 파악을 할 수 있으므로)

row = []     # 완성시킬 줄    
for item in taller:
    _taller, h = item[0], item[1]     # 현재 사람보다 큰 사람의 수, 현재 사람의 키
    if len(row) == 0:     # 줄이 비어 있으면
        row.append([_taller, h])     # 그냥 추가
    else:     # 줄에 누군가가 있다면 키를 비교해서 추가
        if _taller == 0:     # 자신보다 큰 사람이 없다면
            row.insert(0, [_taller, h])     # 줄의 맨 앞에 추가
        else:     # 자신보다 큰 사람이 존재해야 한다면
            cnt = 0     # 현재 사람보다 키가 큰 사람의 수를 살피기 위한 변수
            for p in row:   
                if p[1] < h:     # 줄에 서있는 사람의 키가 현재 사람의 키보다 작을 경우
                    continue     # 그냥 진행
                else:     # 줄어 서있는 사람의 키가 현재 사람의 키보다 클 경우
                    cnt += 1     # cnt 1 증가
                    if cnt == _taller:     # cnt와 현재 사람보다 키가 큰 사람의 수가 같다면     
                        row.insert(row.index(p)+1, [_taller, h])     # p 바로 다음 자리에 현재 사람 삽입
                        break
for p in row:
    print(p[1], end=' ')