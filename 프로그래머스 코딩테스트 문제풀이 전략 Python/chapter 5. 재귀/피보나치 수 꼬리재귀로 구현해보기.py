# 꼬리 재귀 함수 사용
def fib_tail(n, first, second):
    if n <= 1: return second
    return fib_tail(n - 1, second, first + second)