def solution(s):
    l = len(s)
    if l % 2 != 0:
        return s[l//2]
    else:
        return s[l//2-1] + s[l//2]
    
# 다른 풀이
# def string_middle(str):
#     return str[(len(str)-1)//2 : len(str)//2 + 1]     --> 슬라이싱을 사용하면 한번에 작성할 수 있다!