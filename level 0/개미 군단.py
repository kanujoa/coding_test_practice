def solution(hp):
    a = hp // 5
    b = (hp - a*5) // 3
    c = hp - a*5 - b*3
    return a + b + c

# 간단한 풀이
# def solution(hp):    
#     return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)     # 순서대로 장군개미, 병정개미(장군개미 쓰고 남은 것에서 구하기), 일개미(장군, 병정개미 쓰고 최종적으로 남은 것에서 구하기)
