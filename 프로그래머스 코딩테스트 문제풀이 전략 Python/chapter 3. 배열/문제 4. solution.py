def check(place):
    # 2. 문자열(string)을 문자(char)의 배열([])로 생각하여 2중 for문을 작성한다.
    for idx_row, row in enumerate(place):     # idx_row: 행의 index, row: 행 (가로 한 줄)
        for idx_col, cell in enumerate(row):     # idx_col: 열의 index, cell: 한 칸
            if cell != 'P':     # 해당 칸에 사람이 있지 않은 경우
                continue
            # 3. 맨해튼 거리 2 이하 & 파티션의 유무를 고려해 거리두기를 잘했는지 검사한다.
            # 각 상황에서 활용할 인덱스의 범위를 지정해 준다.
            isNotEndRow = idx_row != 4
            isNotEndCol = idx_col != 4
            isNotFirstCol = idx_col != 0
            isBeforeThirdRow = idx_row < 3
            isBeforeThirdCol = idx_col < 3

            # D(Down), D2(2 times Down)
            # R(Right), R2(2 times Right)
            # L(Left)
            # RD(Right - Down), LD(Left - Down)

            if isNotEndRow:     # idx_row가 4가 아니면
                D = place[idx_row + 1][idx_col]     # Down의 위치
                if D == 'P': return 0      # D에 사람이 있으면 0 반환
                if isBeforeThirdRow:     # idx_row가 3 미만이면
                    D2 = place[idx_row + 2][idx_col]     # 2 times Down 위치
                    if D2 == 'P' and D != 'X': return 0     # D2에 사람이 있는데 D에 파티션이 없을 경우 0 반환
                if isNotEndCol:     # idx_col이 4가 아니면
                    R = place[idx_row][idx_col + 1]     # Right의 위치
                    RD = place[idx_row + 1][idx_col + 1]     # RD의 위치 (오른쪽 아래 대각선)
                    if RD == 'P' and (D != 'X' or R != 'X'): return 0     # RD에 사람이 있는데 D나 R에 파티션이 존재하지 않을 경우 0 반환
                if isNotFirstCol:     # idx_col이 0이 아니면
                    L = place[idx_row][idx_col - 1]     # Left의 위치 
                    LD = place[idx_row + 1][idx_col - 1]     # LD의 위치 (왼쪽 아래 대각선)
                    if LD == 'P' and (D != 'X' or L != 'X'): return 0     # LD에 사람이 있는데 D나 L에 파티션이 존재하지 않을 경우 0 반환
            if isNotEndCol:     # idx_col이 4가 아니면 
                R = place[idx_row][idx_col + 1]     # Right의 위치
                if R == 'P': return 0     # R에 사람이 있으면 0을 반환한다. 
                if isBeforeThirdCol:     # idx_col이 3 미만이면
                    R2 = place[idx_row][idx_col + 2]     # 2 times Right의 위치
                    if R2 == 'P' and R != 'X': return 0     # R2에 사람이 있는데 R에 파티션이 존재하지 않을 경우 0 반환

    return 1
                

def solution(places):
    # 1. 주어진 장소(places)의 정보를 받는다.
    return [check(place) for place in places]

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
