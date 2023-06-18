# 이차원 리스트를 활용!

p, m = map(int, input().split())     # 플레이어의 수, 방의 정원
rooms = []

# 각각의 플레이어를 입력 받아 방에 넣어주기 (한줄씩 처리한다!)
for _p in range(p):
    l, n = input().split()
    # 최초 입력된 플레이어
    if not rooms:     # rooms가 비어 있는 리스트이면
        rooms.append([[int(l), n]])
        continue

    # 방에 들어갔는지 확인하는 변수
    enter = False
    # 각 방을 돌면서
    for room in rooms:
        # 조건에 합당하면 넣어주기 (rooms의 요소인 room 리스트 안에 넣는다.)
        if len(room) < m and room[0][0] - 10 <= int(l) <= room[0][0] + 10:
            room.append([int(l), n])
            enter = True
            break
    # 못 들어갔으면 새로운 방을 파서 넣어주기 (rooms의 새로운 리스트 요소가 된다.)
    if not enter:
        rooms.append([[int(l), n]])
    
# 닉네임 기준으로 오름차순 정렬
for room in rooms:
    room.sort(key=lambda x:x[1])

# 정원 수에 따라 출력
for room in rooms:
    if len(room) == m:      # 해당 방이 꽉 차있으면
        print('Started!')     # Started 출력
    else:     # 해당 방에 사람이 모자라면
        print('Waiting!')     # Watiting 출력
    for l, n in room:   
        print(l, n)     # 문구 출력 후 한줄에 하나씩 레벨, 닉네임 출력