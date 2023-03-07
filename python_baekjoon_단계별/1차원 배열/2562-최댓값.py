enumerate() 함수를 이용한 풀이
nums = [int(input()) for _ in range(9)]
idx = 0
max = 0
for i, num in enumerate(nums):
    if num > max:
        max = num
        idx = i
print(max)
print(idx+1)     # 변수명 헷갈리지 않기!     

# index() 메서드와 max() 함수를 이용한 풀이 (코드 길이도 짧고 더 빠름)
# nums = [int(input()) for _ in range(9)]
# print(max(nums))
# print(nums.index(max(nums)) + 1)