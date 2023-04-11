def solution(number, limit, power):
    result = 0
    for a in range(1, number + 1):
        cnt = 0
        for b in range(1, a + 1):
            if a % b == 0:
                cnt += 1
        if cnt > limit:
            result += power
        else:
            result += cnt
    return result

print(solution(5, 3, 2))
print(solution(10, 3, 2))