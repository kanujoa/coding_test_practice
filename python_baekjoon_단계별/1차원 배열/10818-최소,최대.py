import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# 풀어 쓰기
n = int(input())
nums = list(map(int, input().split()))
min = max = nums[0]     # min = nums[0], max = nums[0] 이렇게 따로 적어준 것과 같은 의미!
for i in range(len(nums)):
    if nums[i] < min:
        min = nums[i]
    if nums[i] > max:
        max = nums[i]
print(min, max)