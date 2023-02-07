def solution(n):
    increasing = True
    pizza = 1
    while increasing:
        remain = (6*pizza) % n     # pizza의 값이 달라지면서 remain의 값도 계속 달라져야 하기 때문에 while문 안에 적어줌. 
        if remain != 0:           # remain을 바깥에다 적어주면 맨 처음의 remain이 계속 유지되게 됨.
            pizza += 1
        else:
            increasing = False
    return pizza

print(solution(10))

# 다른 풀이 1 (math 모듈 사용)
# import math

# def solution(n):
#     return (n * 6) // math.gcd(n, 6) // 6    --> math.gcd(a, b)는 a와 b의 최대공약수를 반환한다.

# 다른 풀이 2 (내 풀이를 더 간단하게 작성할 수 있는 방법)
# def solution(n):
#     i=1
#     while(1):     --> while True와 같음.
#         if (6*i)%n==0:     --> 내가 작성한 (6%pizza)%n과 같음.
#             return i
#         i+=1    --> if문이 False일 경우 이것이 실행되고 다시 if문으로 돌아가기 반복
