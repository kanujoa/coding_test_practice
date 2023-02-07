def solution(keyinput, board):
    result = [0, 0]
    range_x = (board[0]-1)/2
    range_y = (board[1]-1)/2
    for drct in keyinput:
        if abs(result[0]) < range_x and abs(result[1]) < range_y:
            if drct == "right":
                result[0] += 1
            elif drct == "left":
                result[0] -= 1
            elif drct == "up":
                result[1] += 1
            elif drct == "down":
                result[1] -= 1
        else:
            pass
    for i in range(2):
        if abs(result[i]) > range_x:
            if result[i] > 0:
                result[i] = (board[i]-1)/2
            else:
                result[i] = -(board[i]-1)/2
    return result
    
print(solution(["left", "left", "left", "right"], [3, 3]))

# 방향키가 순서대로 입력되어야 한다!!!! 그리고 board의 크기를 벗어난 방향키 입력은 '애초에' 무시해 버려야 한다는 조건 꼭 짚고 넘어가야 한다!!
# (테스트 케이스 8번 에러 발생할 경우)
# 반례 : ["left", "left", "left", "right"], [3, 3]
# 기대값 : [0, 0]

# 혹은

# 반례 : ["up", "up", "up", "down"], [3, 3]
# 기대값 : [0, 0]

# 해보세요. 대부분 캐릭터가 맵의 끝에 닿았을 때, 다시 반대쪽 방향키가 입력될 경우 문제가 생기는 것 같네요

# 2. 