def solution(n):
    if (n ** 0.5).is_integer():
        return (n ** 0.5 + 1) ** 2
    return -1

# 한줄로 적기
# def nextSqure(n):
#     return n == int(n**.5)**2 and int(n**.5+1)**2 or -1