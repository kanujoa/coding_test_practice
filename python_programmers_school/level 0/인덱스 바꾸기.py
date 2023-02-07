def solution(my_string, num1, num2):
    str_list = list(my_string)
    str_list[num1], str_list[num2] = str_list[num2], str_list[num1]     # 이렇게 여러개의 요소들을 스와프(swap)하는 것도 가능하다.
    return "".join(str_list)   

# 잘못된 코드
# def solution(my_string, num1, num2):
#     str_list = list(my_string)
#     str_list[num1] = str_list[num2]     --> 여기에서 num1번의 문자를 num2번의 문자로 바꾸면
#     str_list[num2] = str_list[num2]     --> 여기에서 num2번의 문자를 num1번의 문자로 바꾸어야 하는데 num1번의 문자가 이미 num2번의 문자가 되어버렸으므로 그대로이다.
#     return "".join(str_list)

print(solution("hello", 1, 2))