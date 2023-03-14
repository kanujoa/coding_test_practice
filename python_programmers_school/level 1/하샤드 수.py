def solution(x):
    s = sum([int(i) for i in str(x)])
    if x % s == 0:
        return True 
    else:
        return False
    
# 더 간단하게 작성하기
# def Harshad(n):
#     return n%sum(int(x) for x in str(n)) == 0     # 0이면 자동으로 True, 0이 아닐 경우에는 자동으로 False 반환