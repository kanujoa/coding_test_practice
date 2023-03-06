import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
v = int(input())
print(nums.count(v))


# 맨 아래 줄 코드 풀어쓰기
# cnt = 0
# for num in nums:
#     if num == v:
#         cnt += 1
# print(cnt)
