def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4


# 더 좋은 코드
# def solution(angle):
#     answer = (angle // 90) * 2 + (angle % 90 > 0) * 1     범위가 아닌 결과 1, 2, 3, 4에 중점을 둔 코드! 
#     return answer                                         (angle % 90 > 0)은 True or False이기 때문에 0 or 1로 계산된다.