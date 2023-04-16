def solution(n):
    cnt = 0
    for i in range(n // 2 + 1):
        tmp = []
        for _ in range(i):
            tmp.append(2)
        for _ in range(n - i * 2):
            tmp.append(1)
        if len(set(tmp)) == 1:
            cnt += 1
        elif len(tmp) == 2:
            cnt += 2
        else:
            cnt += len(tmp) * (len(tmp) - 1) // 2
    return cnt

print(solution(2))
print(solution(5))