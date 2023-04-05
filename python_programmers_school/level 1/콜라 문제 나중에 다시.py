def solution(a, b, n):
    result = 0
    while n > 2:
        result += n // a * b
        n = n - n // a * a + n // a * b
    result += n // a * b
    n = n - n // a * a + n // a * b
    return result

# print(solution(2, 1, 20))
# print(solution(3, 1, 20))
print(solution(3, 2, 20))