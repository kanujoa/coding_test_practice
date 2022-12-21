def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
        else:
            pass
    return answer

print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))


# 더 좋은 코드
# def solution(n, numlist):
#     return list(filter(lambda v: v%n==0, numlist))

# filter 함수: filter(함수, [object]) 형식으로 사용
# 두 번째 인자로 넘어온 데이터 중에서 첫 번째 인자로 넘어온 조건 함수를 만족하는 데이터만 반환함.