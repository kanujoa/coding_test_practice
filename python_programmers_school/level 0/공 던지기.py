def solution(numbers, k):
    result = 2*k -1
    if result > len(numbers):
        while result > len(numbers):      # len(numbers) 대신에 numbers[-1]로 작성하기 가능!
            result -= len(numbers)
        return result
    else:
        return result

# 다른 풀이 1
# def solution(numbers, k):
#     return numbers[2 * (k - 1) % len(numbers)]     --> 인덱싱에 중점을 두어 짠 코드

# 다른 풀이 2
# def solution(numbers, k):
#     return 2 * (k - 1) % numbers[-1] + 1      --> 결과 숫자에 중점을 두어 짠 코드