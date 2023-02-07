import math

def solution(n):
    if str(math.sqrt(n)).split(".")[1] == '0':
        return 1
    else:
        return 2

print(solution(144))
print(solution(976))

# 다른 좋은 코드
# def solution(n):
#     return 1 if (n ** 0.5).is_integer() else 2