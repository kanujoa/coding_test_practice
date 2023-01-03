def solution(my_string):
    answer = [int(i) for i in my_string if i.isdigit() == True]
    return sorted(answer)

# 비슷한 풀이
# def solution(my_string):
#     return sorted([int(c) for c in my_string if c.isdigit()])     --> True는 꼭 적어주지 않아도 되고 변수를 사용하지 않고 바로 return 옆에 적어
#                                                                       줄 수도 있다.