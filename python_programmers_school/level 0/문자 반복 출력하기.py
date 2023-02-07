def solution(my_string, n):
    repeat = [i*n for i in my_string]
    return "".join(repeat)

# 다른 사람의 풀이
# def solution(my_string, n):
#     return ''.join(i*n for i in my_string)     --> 이렇게 한줄로 적어주어도 된다.