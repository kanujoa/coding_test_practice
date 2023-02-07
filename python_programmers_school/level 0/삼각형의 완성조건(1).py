def solution(sides):
    sides.sort()
    if sides[-1] < sides[0] + sides[1]:
        return 1
    else:
        return 2


print(solution([1, 2, 3]))

# 다른 풀이
# def solution(sides):
#     return 1 if max(sides) < (sum(sides) - max(sides)) else 2
