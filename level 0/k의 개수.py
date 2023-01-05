def solution(i, j, k):
    num = [str(num) for num in range(i, j+1)]
    join_num = "".join(num)
    return join_num.count(str(k))

print(solution(1, 13, 1))

# 짧은 풀이
# def solution(i, j, k):
#     answer = sum([str(i).count(str(k)) for i in range(i,j+1)])     --> 주어진 범위에서 각 숫자 안에 있는 k의 개수를 세어 모두 더하는 코드
#     return answer