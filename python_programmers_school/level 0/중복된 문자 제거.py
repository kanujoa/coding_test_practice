def solution(my_string):
    answer = ''
    for s in my_string:
        if s in answer:
            pass
        else:
            answer += s
    return answer

# 간단한 풀이
# def solution(my_string):
#     return ''.join(dict.fromkeys(my_string))     --> 아래의 dict_1 형태로 딕셔너리 생성, 딕셔너리에서는 동일한 key를 작성할 수 없으므로 그것을 이용
#                                                  --> 또한 딕셔너리에서도 join 함수 사용 가능 (딕셔너리에서 join 함수를 쓰면 key끼리만 합쳐짐. value가 다 달라도 사용 가능)   
# dict.fromkeys 함수: 딕셔너리 생성 시 편하게 사용 가능
# 예시
# seq = ('name', 'age', 'sex')

# dict_1 = dict.fromkeys(seq)
# print(dict_1)

# dict_2 = dict.fromkeys(seq, 10)
# print(dict_2)

# {'age':None, 'name':None, 'sex':None}
# {'age':10, 'name':10, 'sex':10}