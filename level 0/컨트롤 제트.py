def solution(s):
    rmv_blank = s.split()
    a = 0
    for i in range(len(rmv_blank)):
        if rmv_blank[i] != 'Z':
            a += int(rmv_blank[i])
        elif rmv_blank[i] == 'Z':
            a -= int(rmv_blank[i-1])
    return a

# 더 좋은 코드