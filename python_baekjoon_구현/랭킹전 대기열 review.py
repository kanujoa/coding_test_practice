p, m = map(int, input().split())     # 플레이어의 수, 방의 정원
rooms = []     # 여러 개의 방들이 들어갈 리스트

# 방 구성하기
for _ in range(p):
    lv, name = input().split()
    if len(rooms) == 0:     # rooms 리스트에 방이 하나도 없는 경우
        rooms.append([[int(lv), name]])      # 새 방을 만듦과 동시에 현재 player 정보 넣기
    else:     # 이미 방이 존재하는 경우
        for room in rooms:      # 방을 0번부터 하나씩 탐색
            first_lv = room[0][0]     # 각 방에 처음 입장한 player의 레벨
            if len(room) < m and first_lv - 10 <= int(lv) <= first_lv + 10:     # 방의 정원이 꽉 차있지 않으면서 현재 player의 레벨이 first_lv의 +-10 범위에 있다면
                room.append([lv, name])     # 그 방에 현재 player 입장
                break     # 입장이 완료되면 반복문 종료
        else:     # 조건에 맞지 않아 위에서 break가 걸리지 않은 경우
            rooms.append([[int(lv), name]])     # 새로운 방을 파야 함.
    
# 각 방 상태를 탐색하며 정원이 꽉 차있는 경우에는 started, 모자란 경우에는 waiting 출력한 후 각 방의 player들도 같이 출력
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(key=lambda x:x[1])     # 닉네임이 사전 순으로 앞선 player부터 출력해야 하므로 닉네임을 오름차순으로 정렬해 주었다.
    for player in room:
        print(player[0], player[1])