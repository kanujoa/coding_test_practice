t = int(input())     # 테스트 케이스의 개수

for _ in range(t):
    # 북: 0, 동: 1, 남: 2, 서: 3 으로 설정 
    d = 0     # 처음에는 북쪽 방향을 바라보고 있음
    r, c = 0, 0     # 처음에는 (0, 0)부터 시작 (r = 행, c = 열)
    f = [[-1, 0], [0, 1], [1, 0], [0, -1]]     # 앞으로 이동 명령일 경우 r좌표와 c좌표가 얼만큼 움직여야 하는지 기록
    b = [[1, 0], [0, -1], [-1, 0], [0, 1]]     # 뒤로 이동 명령일 경우 위와 동일한 역할을 하는 리스트
    r_history = [0]     # 거북이가 거쳤던 r 좌표들을 기록하는 역할
    c_history = [0]     # 거북이가 거쳤던 c 좌표들을 기록하는 역할

    commands = input()     # 이동 명령 받기

    for command in commands:
        if command == 'F':     # 앞으로 가라는 명령일 때
            new_r = r + f[d][0]
            new_c = c + f[d][1]
            r, c = new_r, new_c
            r_history.append(r)
            c_history.append(c)
        elif command == 'B':     # 뒤로 가라는 명령일 때
            new_r = r + b[d][0]
            new_c = c + b[d][1]
            r, c = new_r, new_c
            r_history.append(r)
            c_history.append(c)
        elif command == 'L':     # 뒤로 가라는 명령일 때 왼쪽으로 90도 회전
            if d > 0:
                d -= 1
            else:
                d = 3
        elif command == 'R':     # 앞으로 가라는 명령일 때 오른쪽으로 90도 회전
            if d < 3:
                d += 1
            else:
                d = 0

    width = max(c_history) - min(c_history)     # 직사각형의 너비
    height = max(r_history) - min(r_history)     # 직사각형의 높이

    print(width * height)     # 거북이가 이동한 영역을 모두 포함하는 작은 직사각형의 넓이를 출력