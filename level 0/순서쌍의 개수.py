def solution(n):
    div = [num for num in range(1, n+1) if n%num == 0]
    return len(div)     # 순서쌍의 개수는 n의 약수의 개수와 같다.


# 안좋은 코드
# def solution(n):
#     pair = []
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             if a * b == n:
#                 pair.append((a, b))
#             else:
#                 pass
#     return len(pair)     --> 이렇게 반복이 많은 코드는 숫자의 범위가 매우 커졌을때는 시간초과가 되어버린다.


# 다른 풀이
# def solution(n):
#     return len(list(filter(lambda v: n % (v+1) == 0, range(n))))     --> 이렇게 한줄로 적어줄 수 있다.
# filter 함수는 두 번째 인자로 넘어온 데이터 중에서 첫 번째 인자로 넘어온 조건 함수를 만족하는 데이터만 반환한다.