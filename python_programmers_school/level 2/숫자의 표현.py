def solution(n):
    way = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                way += 1
                break
            elif sum > n:
                break
    return way

print(solution(15))