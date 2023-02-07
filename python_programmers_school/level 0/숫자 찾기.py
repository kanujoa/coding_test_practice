def solution(num, k):
    if str(k) in str(num):
        return str(num).index(str(k))+1
    else:
        return -1

# 짧은 풀이
# def solution(num, k):
#     return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1     --> 이렇게 한 줄로 적어줄 수도 있다. 
#               (find 함수는 index 함수와 비슷하게 인자로 들어가는 문자열의 처음 시작 위치를 반환한다. 따라서 문자열의 길이가 2 이상이어도 된다.)

# 다른 풀이 (enumerate 사용: enumerate 함수를 사용하여 for문을 돌려보면 (인덱스, 리스트의 원소) 이렇게 튜플 형태로 담겨 있는 것을 확인 가능)
# def solution(num, k):
#     for i, n in enumerate(str(num)):     --> i는 index에, n은 리스트의 원소에 해당 (아래 코드는 내가 작성한 것과 같은 원리)
#         if str(k) == n:
#             return i + 1
#     return -1
