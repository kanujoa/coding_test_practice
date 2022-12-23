def solution(num1, num2):
    answer = int(str(num1 / num2 * 1000).split(".")[0])
    return answer

# 더 좋은 풀이
# def solution(num1, num2):
#     return int(num1 / num2 * 1000)     그냥 int()만 써주면 자동으로 소숫점 아래 부분은 사라지고 정수 부분만 남음.