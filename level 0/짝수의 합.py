def solution(n):
    even_num = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even_num.append(i)
    return sum(even_num)


# 더 간단한 풀이
# def solution(n):
#     return sum([i for i in range(2, n + 1, 2)])
