def solution(array, commands):
    res = []
    for c in commands:
        cut = sorted(array[c[0]-1:c[1]])
        res.append(cut[c[2]-1])
    return res

# 간략한 풀이
# def solution(array, commands):
#     return [sorted(array[a-1:b])[c-1] for a,b,c in commands]