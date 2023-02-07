def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        else:
            return 4
    if dot[0] < 0:
        if dot[1] > 0:
            return 2
        else:
            return 3

# 다른 사람의 풀이
# def solution(dot):
#     quad = [(3,2),(4,1)]     --> dot[0](x좌표)이 0보다 작은것끼리, 큰것끼리 묶음
#     return quad[dot[0] > 0][dot[1] > 0]     --> []안에 있는 코드가 True면 1이, False면 0이 들어갈 것임.