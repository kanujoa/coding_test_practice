def solution(n):
    num = []
    for i in str(n):
        num.append(int(i))
    return sum(num)
    
print(solution(1234))
print(solution(930211))

# 더 좋은 코드
# def solution(n):
#     answer = sum(list(map(int,list(str(n))))
#     return answer