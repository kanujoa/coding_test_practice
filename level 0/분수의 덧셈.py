from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    fraction = Fraction(denum1 * num2 + denum2 * num1) / Fraction(num1 * num2)     # 부동소수점 문제때문에 Fraction으로 한번에 묶지 않고 나누어서 묶어줌.
    return [fraction.numerator, fraction.denominator]

print(solution(9, 2, 1, 3))

# Fraction 모듈 더 간단히 이용하기
# from fractions import Fraction

# def solution(denum1, num1, denum2, num2):
#     answer = Fraction(denum1, num1) + Fraction(denum2, num2)
#     return [answer.numerator, answer.denominator]


# math 모듈 이용하기
# import math

# def solution(denum1, num1, denum2, num2):
#     denum = denum1 * num2 + denum2 * num1
#     num = num1 * num2
#     gcd = math.gcd(denum, num)     math.gcd는 denum과 num 사이의 최대공약수를 찾아준다.
#     return [denum//gcd, num//gcd]     


# 최대공약수 구해서 분모 분자 숫자를 그것으로 나누어서 푸는 방법
# def solution(denum1, num1, denum2, num2):
#     answer = []
#     s = 0

#     denum0 = (denum1*num2) +(denum2*num1)
#     num0 = num1*num2

#     for i in range(min(denum0,num0),0,-1):
#         if denum0%i == 0 and num0%i == 0:
#             s = i
#             break

#     denum0 /= s
#     num0 /= s
#     answer.append(denum0)
#     answer.append(num0)

#     return answer