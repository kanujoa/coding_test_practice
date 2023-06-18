import sys
input = sys.stdin.readline

# N: 방의 세로 크기, M = 방의 가로 크기
N, M = map(int, input().split())
# r, c, d: 청소기의 시작 위치와 방향
r, c, d = map(int, input().split())     # r이 행, c가 열을 뜻함!
# room: 방의 상태
room = [list(map(int, input().split())) for _ in range(N)]

# 탐색 방향 (북, 동, 남, 서쪽을 보고 있을 때의 왼쪽 탐색)
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 방 청소 함수 선언
def clean(r, c, d, room):
    
    # cnt: 청소한 칸의 개수
    # 출발 지점 청소 및 cnt 세주기
    room[r][c] = -1
    cnt = 1

    # 멈출 때까지 청소
    while True:
        # 왼쪽 회전
        nr = r + dr[d]
        nc = c + dc[d]

        # 청소되지 않은 영역일 경우
        if room[nr][nc] == 0:
            # 청소기 이동 후 청소
            r = nr
            c = nc
            room[r][c] = -1
            # 회전한 방향 반영
            if d == 0:
                d = 3
            else:
                d -= 1
            # cnt 세주기
            cnt += 1
          
        # 이미 청소한 영역이거나 벽일 경우
        else:
            # 나머지 3 방향 탐색 (dr, dc에서 인덱스가 왼쪽으로 향해야 한다. 0에 도달하면 끝에서부터 다시 왼쪽으로)
            for i in range(1, 4):
                if d - i < 0:
                    nd = d - i + 4
                else:
                    nd = d - i
            
                # 청소하지 않은 곳이 있을 경우 해당 방향으로 회전 후 다시 청소 진행
                nr = r + dr[nd]
                nc = c + dc[nd]
                if room[nr][nc] == 0:
                    d = nd
                    break     # 다시 while문(위로) 가서 칸을 해당 방향에 위치하는 쪽으로 1칸 옮김.
            
            # 탐색 결과 청소하지 않은 곳이 없을 경우
            else:
                # 바로 뒤 탐색
                nd = (d + 3) % 4      # nd는 반시계 90도 회전을 수행하기 전 원래 방향으로 되돌아가는 것임! 위 if문을 수행하고 나면 위치가 90도 시계방향에 있으므로 
                nr = r + dr[nd] 
                nc = c + dc[nd]
                # 벽일 경우 청소 종료
                if room[nr][nc] == 1:
                    break
                else:
                    r = nr
                    c = nc
    
    # 청소한 칸의 개수 출력 후 반환
    print(cnt)
    return

# 함수 실행
clean(r, c, d, room)