def solution(brown, yellow):
    extent = brown + yellow
    for w in range(extent, 0, -1):
        if extent % w == 0:
            h = extent // w
            if (w * 2) + ((h-2) * 2) == brown:
                return [w, h]
            
print(solution(10, 2))


# 다른 풀이
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]