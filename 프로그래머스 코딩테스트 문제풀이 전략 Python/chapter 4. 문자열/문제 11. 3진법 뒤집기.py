def solution(n):
    tenary_reverse = ''
    while n != 0:
        tenary_reverse += str(n % 3)
        n = n // 3
    return int(tenary_reverse, 3)

print(solution(45))