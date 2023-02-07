def solution(n):
    answer = [i for i in range(1,n+1) if i%2!=0]
    return answer

# 더 간단한 풀이
# def solution(n):
#     return [i for i in range(1, n+1, 2)]      range 함수를 효율적으로 사용하면 좋다!