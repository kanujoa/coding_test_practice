def solution(n):
    res = 0
    for i in range(1, n+1):     
        if n % i == 0:
            res += i
    return res

# 반 넘어가는 지점은 탐색하지 않아도 된다! 자기 자신 이전에서 최대로 큰 약수는 자기 자신을 반으로 나눈 값이 되기 때문!
# def solution(num):
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
