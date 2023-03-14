def solution(num):
    if num % 2 == 1:
        return "Odd"
    else:
        return "Even"

# 간단한 풀이
# def evenOrOdd(num):
#     if num%2:
#         return "Odd"

#     return "Even"

# 다른 풀이
# def evenOrOdd(num):
#     return ["Even", "Odd"][num & 1]     --> 비트 연산자 사용(num & 1의 결과가 1이면 Odd(홀수), 아니면 Even(짝수))