from itertools import combinations

def solution(nums):
    c = list(combinations(nums, 3))
    l = list(map(sum, c))     # 합이 중복되어도 하나로 취급하지 않으므로 여기서 set이 아니라 list를 사용해야 통과된다.
    cnt = 0
    for i in l:
        for j in range(2, i//2+1):
            if i % j == 0:
                break
        else:
            cnt += 1
    return cnt  

print(solution([1,2,3,4]))