# 반복문으로 구현
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i

print(result)    


# 재귀로 구현
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else: 
        return 1

print(factorial(int(input())))
