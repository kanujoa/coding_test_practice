# 윗줄과 아래줄을 슬라이싱으로 가져오면 코드의 길이가 짧아진다.

def solution(rows, columns, queries):
    answer = []
    board = [[columns * j + (i + 1) for i in range(columns)] for j in range(rows)]

    for query in queries:
        # a == x1, b == y1, c == x2, d == y2 라고 생각하면 됨.
        a, b, c, d = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        # row1 == 윗줄(맨 오른쪽 칸 제외), row2 == 아랫줄(맨 왼쪽 칸 제외)임.
        row1, row2 = board[a][b:d], board[c][b + 1: d + 1]
        # 오른쪽 줄 (위의 숫자를 아래로 한 칸 내림.)
        for i in range(c, a, -1):
            board[i][d] = board[i - 1][d]
            if board[i][d] < _min: _min = board[i][d]
        # 왼쪽 줄 (아래의 숫자를 위로 한 칸 올림.)
        for i in range(a, c):
            board[i][b] = board[i + 1][b]
            if board[i][b] < _min: board[i][b]

        # 회전하여 변한 윗줄과 아랫줄을 board에 적용해 준다.
        board[a][b + 1: d + 1], board[c][b:d] = row1, row2

        answer.append(_min)

    return answer