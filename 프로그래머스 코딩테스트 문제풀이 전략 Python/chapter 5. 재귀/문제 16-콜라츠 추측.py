# 반복 횟수를 도출하기 위해 변수에 num 뿐만 아니라 cnt도 작성했다.

def collatz(num, cnt):
    if num == 1: 
        return cnt
    elif cnt > 500:
        return -1
    elif num % 2 == 0:
        return collatz(num // 2, cnt + 1)
    else:
        return collatz(num * 3 + 1, cnt + 1)

def solution(num):
    return collatz(num, 0)

print(solution(6))
