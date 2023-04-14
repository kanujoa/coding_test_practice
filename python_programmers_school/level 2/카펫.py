def solution(brown, yellow):
    extent = brown + yellow
    for w in range(extent, 0, -1):
        if extent % w == 0:
            h = extent // w
            if (w * 2) + ((h-2) * 2) == brown:
                return [w, h]
            
print(solution(10, 2))