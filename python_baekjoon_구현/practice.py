import sys
input = sys.stdin.readline

# N: 방의 세로 크기, M: 방의 가로 크기
N, M = map(int, input().split())
# r, c, d: 청소기의 시작 위치와 방향
r, c, d = map(int, input().split())
# room: 방의 상태
room = [list(map(int, input().split())) for _ in range(N)]

# 탐색 방향(북쪽, 동쪽, 남쪽, 서쪽을 보고 있을 때의 왼쪽 탐색)
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
            # 나머지 3 방향 탐색
            for i in range(1, 4):
                if d - i < 0:
                    nd = d - i + 4
                else:
                    nd = d - i

                # 청소하지 않은 곳이 있을 경우 해당 방향으로 회전 시켜주고 다시 청소 진행
                nr = r + dr[nd]
                nc = c + dc[nd]
                if room[nr][nc] == 0:
                    d = nd                
                    break

            # 탐색 결과 청소하지 않은 곳이 없을 경우
            else:
                # 바로 뒤 탐색
                nd = (d + 3) % 4
                nr = r + dr[nd]
                nc = c + dc[nd]
                # 벽일 경우 청소 종료
                if room[nr][nc] == 1:
                    break
                # 벽이 아닐 경우 해당 위치로 이동
                else:
                    r = nr
                    c = nc

    # 청소한 칸의 개수 출력 후 반환
    print(cnt)
    return

# 청소 실시!
clean(r, c, d, room)