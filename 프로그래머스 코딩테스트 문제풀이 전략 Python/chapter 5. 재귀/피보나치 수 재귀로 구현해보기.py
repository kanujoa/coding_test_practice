# 재귀 함수 사용
def fib_rec(n):
    if n < 3: return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

# 상태 관리 변수를 사용하지 않고, 함수의 상태를 나타내는 변수를 인자로 받아 사용자가 관리할 필요 없이 함수
# 내부에서 모두 처리할 수 있게 되었다.

print(fib_rec(3))