def solution(box, n):
    a = box[0]//n
    b = box[1]//n
    c = box[2]//n
    
    return a * b * c

print(solution([10, 8, 6], 3))

# 다른 풀이 1 (for문 사용)
# def solution(box, n):
#     answer = 1
#     for b in box:
#         answer *= b // n
#     return answer

# 다른 풀이 2 (내가 하려고 했던 방법)
# def solution(box, n):
#     return (box[0] // n) * (box[1] // n) * (box[2] // n)     --> 이 방법을 쓰려면 '괄호'로 묶어주어야지 계산 순서가 제대로 됨!!