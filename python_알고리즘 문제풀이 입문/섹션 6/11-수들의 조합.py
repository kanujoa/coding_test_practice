n, k = map(int, input().split())     # n : 정수의 개수, k : 임의의 정수 (뽑을 정수의 개수)
nums = list(map(int, input().split()))     # n개의 정수 리스트
m = int(input())     # 합이 m의 배수인지 확인하기 위해

def DFS(L, s):
    global cnt
    if L == k:
      if sum(combination) % m == 0:
        cnt += 1
      else: return
    else:
        for i in range(s, len(nums)):
            combination[L] = nums[i]
            DFS(L + 1, i + 1)

combination = [0] * (n + 1)
cnt = 0
DFS(0, 0)
print(cnt)