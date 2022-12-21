def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]
        answer = common[-1] + d
    elif common[1] / common[0] == common[2] / common[1]:
        r = common[1] / common[0]
        answer = common[-1] * r
    return int(answer)

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))

# 다른 좋은 코드
# def solution(common):
#     answer = 0
#     a,b,c = common[:3]
#     if (b-a) == (c-b):
#         return common[-1]+(b-a)
#     else:
#         return common[-1] * (b//a)
#     return answer