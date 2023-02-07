def solution(array):
    answer = 0
    for num in array:
        for i in range(len(str(num))):
            if "7" in list(str(num))[i]:
                 answer += 1
            else:
                pass
    return answer

print(solution([7, 77, 17]))
print(solution([10, 29]))

# 더 좋은 코드
# def solution(array):
#     return str(array).count('7')     count 함수 사용!