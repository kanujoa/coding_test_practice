# 반복문 사용
def fib(n):
    calc = [1, 1]
    for i in range(2, n):
        calc.append(calc[i - 1] + calc[i- 2])
    
    return calc[n - 1]

print(fib(3))

# 피보나치 수열을 배열로 구현하면 값을 가지고 있을 배열 하나, n까지 반복 횟수를 위한 변수 하나 이렇게
# 상태 관리를 위한 변수가 총 2개 사용된다.

