import statistics

def solution(array):
    return statistics.median(array)

print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))


# 내가 만든 다른 풀이
# def solution(array):
#     ascending = sorted(array)
#     median_num = (len(array) - 1) // 2
#     median = ascending[median_num]
#     return median