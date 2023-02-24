N, M = map(int, input().split())
A = list(map(int, input().split()))

p1 = 0
p2 = p1
sum = A[p1]
count = 0
while p1 < N and p2 < N:
  if sum == M:
    count += 1
    p1 += 1
    sum = A[p1]
    p2 = p1
  elif sum > M:
    p1 += 1
    sum = A[p1]
    p2 = p1
  else:
    p2 += 1
    if p2 == N:
      break
    else:
      sum += A[p2]
print(count)