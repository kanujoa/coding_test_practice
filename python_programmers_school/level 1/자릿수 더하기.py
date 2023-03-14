def solution(n):
    return sum(list(int(i) for i in str(n)))

# 다른 풀이 (반복문 말고 재귀 이용)
# def sum_digit(number):
#     if number < 10:
#         return number

#     return number%10 + sum_digit(number//10)     

# print(sum_digit(123))