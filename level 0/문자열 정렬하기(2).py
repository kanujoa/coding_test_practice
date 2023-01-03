def solution(my_string):
    return "".join(sorted([i.lower() for i in my_string]))

# 더 간단한 풀이
# def solution(my_string):
#     return ''.join(sorted(my_string.lower()))     --> sorted 함수는 문자열에도 사용이 가능함. 대신, 문자열을 오름차순으로 정렬한 결과를 리스트에 담아서 보여줌.