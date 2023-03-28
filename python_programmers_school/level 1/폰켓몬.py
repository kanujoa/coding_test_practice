def solution(nums):
    select = len(nums) // 2
    cnt = 0
    prev = []
    for n in nums:
        if select == 0:
            break
        if n not in prev:
            prev.append(n)
            cnt += 1
            select -= 1
    return cnt

# 간단한 풀이
# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))     --> 절반을 가져가라 했으므로 그 절반이 nums 구성 요소들의 개수보다 적으면 그것이 답
# --> 절반이 nums 구성 요소들의 개수보다 많으면 구성 요소의 개수들이 답