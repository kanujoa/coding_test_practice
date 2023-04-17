def solution(n):
    return sum([d for d in range(1, n+1) if n % d == 0])

# 풀어서 작성하기 
def solution(n):
    answer = 0
    for d in range(1, n+1):
        if n % d == 0:
            answer += d
    return answer

# 다른 사람 풀이 1
# 연산 더 적게 하기 (range 주목!)
def solution(n):
    return sum([d for d in range(1, n // 2 + 1) if n % d == 0]) + n