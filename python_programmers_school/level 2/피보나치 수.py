def solution(n):
    process = [0, 1]
    for _ in range(2, n+1):
        process.append(process[-1] + process[-2])
    return process[-1] % 1234567    

print(solution(3))


# 메모리를 더 적게 사용하는 코드
def fibonacci(num):
    a, b = 0, 1     # a, b는 초깃값 각각 0(F(0)), 1(F(1))
    for i in range(num):    
        a, b = b, (a+b) % 1234567     # 리스트를 만들지 않고 a와 b에 할당될 값을 바꾸어 주었다.
    return a

print(fibonacci(3))