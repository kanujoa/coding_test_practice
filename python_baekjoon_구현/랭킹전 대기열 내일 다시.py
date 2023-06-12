p, m = map(int, input().split())     # 플레이어의 수, 방의 정원

players = []     # 입장 신청 목록
for _ in range(p):
    l, n = input().split()     # 플레이어의 레벨, 닉네임
    players.append([l, n, 'f'])     

first = 0     # 방이 생성될 때 처음 입장한 사람의 레벨
room = []     # 한 방에 들어가는 플레이어들을 담는 리스트
cnt = 0
i = 0
while cnt != m:
    player = players[i]
    l, n = int(player[0]), player[1]
    if len(room) == 0:
        print('Started!')
        first = l
        room.append(player)
        cnt += 1
    else:
        if first - 10 <= l <= first + 10:
            room.append(player)
            cnt += 1
        else:
            i += 1
    if len(room) == m:
        room.sort(key=lambda x:x[1])
        for player in room:
            l, n = player[0], player[1]
            print(l, n)
        i = 0
        room.clear()
    if 0 < len(players) < m and len(room) == 0:
        print('Waiting!')
        players.sort(key=lambda x:x[1])
        for player in players:
            l, n = player[0], player[1]
            print(l, n)
        break