def solution(my_string):
    result = []
    for i in my_string:
        if i.isupper():
            result.append(i.lower())
        else:
            result.append(i.upper())
    return "".join(result)

print(solution("cccCCC"))

# 잘못된 코드
# def solution(my_string):
#     for i in my_string:
#         if i.isupper():
#             my_string = my_string.replace(i, i.lower())     --> my_string 안에 똑같은 i값이 여러개 존재한다면 그것들을 모두 한꺼번에 소문자로 바꿈
#         else:
#             my_string = my_string.replace(i, i.upper())     --> 이것도 마찬가지
#     return my_string     (따라서 "cccCCC"에서 오류가 발생한다. 겹치는 문자가 없는 "abCdEfghIJ"에서는 오류가 발생하지 않는다.)

# 다른 풀이
# def solution(my_string):
#     return my_string.swapcase()     --> swapcase() 함수는 문자열의 대문자는 소문자로, 소문자는 대문자로 각각 바꾸어 주는 함수이다.

