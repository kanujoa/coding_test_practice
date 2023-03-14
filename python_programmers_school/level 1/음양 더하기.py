def solution(absolutes, signs):
    z = list(zip(absolutes, signs))
    result = 0
    for i in z:
        if i[1] == True:
            result += i[0]
        else:
            result += i[0] * -1
    return result

# 조금 더 간단히 적기
# def solution(absolutes, signs):
#     answer=0
#     for absolute,sign in zip(absolutes,signs):     --> absolute와 sign에 (absolutes, sign) 안의 요소를 하나씩 차례로 할당
#         if sign:
#             answer+=absolute
#         else:
#             answer-=absolute     --> * -1 할 필요 없이 -=로 해주면 간단
#     return answer