def solution(slice, n):
    if n % slice != 0:
        return n // slice + 1
    else:
        return n // slice

# 더 좋은 풀이
# def solution(slice, n):
#     return ((n - 1) // slice) + 1     --> 모든 경우에 들어맞음!
