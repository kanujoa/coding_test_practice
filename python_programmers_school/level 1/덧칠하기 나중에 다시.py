def solution(n, m, section):
    paint = []
    result = 0
    l = 0
    r = len(section)-1
    while len(paint) != len(section):
        if result % 2 == 0:
            for s in section:
                if s in range(section[l], section[l]+m):
                    if s not in paint:
                        paint.append(s)
            result += 1
            l += 1
        else:
            for s in section:
                if s in range(section[r]-m+1, section[r]+1):
                    if s not in paint:
                        paint.append(s)
            result += 1
            r -= 1
    return result

print(solution(8, 4, [2, 3, 6]))