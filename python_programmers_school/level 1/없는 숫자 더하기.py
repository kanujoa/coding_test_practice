def solution(numbers):
    a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    return sum(list(a - set(numbers)))

# 간단한 풀이
# def solution(numbers):
#     return 45 - sum(numbers)     --> 0부터 9까지의 수를 모두 더한 값인 45에서 numbers 리스트의 수를 모두 더한 값을 빼면 바로 답이 나옴.

# 람다 함수 사용한 간단한 풀이
# solution = lambda x: sum(range(10)) - sum(x)
