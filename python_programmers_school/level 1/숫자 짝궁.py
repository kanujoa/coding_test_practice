def solution(X, Y):
    answer = ''
    # answer에 들어갈 수를 구하는 과정
    for i in set(X):     # i는 X의 구성 요소 (set을 썼으므로 중복 X)   
        if X.count(i) >= Y.count(i):     # X에서 i를 센 값이 Y에서 i를 센 값보다 크거나 같다면
            answer += i * Y.count(i)     # Y에서 i를 센 값이 i의 개수가 되고, 그 개수만큼 answer에 i를 더한다. (문자열) (겹치는 만큼만 짝궁이 되므로!)
        else:     # Y에서 i를 센 값이 더 많을 경우
            answer += i * X.count(i)     # X에서 i를 센 값이 i의 개수가 되고, 그 개수만큼 answer에 i를 더한다. (문자열) (겹치는 만큼만 짝궁이 되므로!)
    # answer의 값에 따라 반환할 값을 구하는 과정
    if answer == '':     # answer가 빈 값인 경우 
        return '-1'     # 짝궁이 없는 경우이므로 -1 반환
    elif set(answer) == {'0'}:     # answer의 구성 요소가 '0' 밖에 없는 경우
        return '0'     # '0' 반환
    else:     # 나머지 보통의 경우
        return ''.join(sorted(answer, reverse=True))     # 최대의 수를 구해야 하므로 answer의 구성 요소를 내림차순 정렬 뒤 문자열로 만드는 과정을 거쳤다.


# 일부 테스트 케이스에서 시간 초과
# def solution(X, Y):
#     answer = ''
#     for i in X:
#         if Y.count(i) != 0:
#             answer += i
#             Y = Y.replace(i, '', 1)
#     sort = sorted(answer, reverse=True)
#     if len(sort) != 0:
#         if set(sort) == {'0'}:
#             return '0'
#         else:
#             return ''.join(sort)
#     else:
#         return '-1'       


# 맨 위 풀이 더 간단하게 작성하기
from collections import Counter     # Counter 안쓰고 그냥 count 사용해도 됨.

def solution(X, Y):
    answer = ''
    X = Counter(X)
    Y = Counter(Y)

    for i in range(9, -1, -1):     # i의 범위를 9부터 -1까지 -1 간격으로 설정
        answer += (str(i) * min(X[str(i)], Y[str(i)]))      # X 에서의 str(i)의 개수와 Y에서의 str(i)의 개수 중 더 작은 수만큼 str(i)를 answer에 더한다.
    
    if answer == '':
        return '-1'
    elif len(answer) == Counter(answer)['0']:
        return '0'
    else:
        return answer
    
print(solution("100", "2345"))
print(solution("100", "123450"))