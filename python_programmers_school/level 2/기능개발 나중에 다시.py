import math
from collections import deque

def solution(progresses, speeds):
    result = []
    
    days = deque()
    for i in range(len(progresses)):
        remain = 100 - progresses[i]
        days.append(math.ceil(remain / speeds[i]))
    
    l = 0
    r = 1
    remove = 0
    while len(days) != 1:
        if days[l] < days[r]:
            if remove != 0:
                result.append(remove)
                remove = 0
            for _ in range(r-l):
                days.popleft()
                remove += 1
            result.append(remove)
            remove = 0
        elif days[l] == days[r]:
            for _ in range(r-l):
                days.popleft()
                remove += 1
        else:
            r += 1
    remove += 1
    result.append(remove)
            
    return result

# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))
# print(solution([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7]))
# print(solution([90, 90, 90, 90],[30, 1, 1, 1]))