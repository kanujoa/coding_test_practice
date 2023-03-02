N, M = map(int, input().split())     # N은 입력한 숫자의 개수, M은 더해서 나와야 할 수
numbers = list(map(int, input().split()))     # 입력한 수를 리스트로 바꾸기

cnt = 0
for i in range(N):
  for j in range(i+1, N+1):
    s = 0
    for idx in range(i, j):
      s += numbers[idx] 
    if s == M:
      cnt += 1
      break
    elif s > M:
      break

print(cnt)     # 역시 시간 초과

# cnt = 0
# for i in range(N):
#   for j in range(i+1, N+1):
#     if sum(numbers[i:j]) == M:
#       cnt += 1
# print(cnt)     --> 이렇게 하면 많은 수를 입력으로 넣었을 때 시간 초과!
