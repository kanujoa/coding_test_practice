N = int(input())
num = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
rotate = [list(map(int, input().split())) for _ in range(M)]

# 회전명령 수행
for cmd in rotate:
  row = cmd[0] - 1
  dir = cmd[1]
  cnt = cmd[2]
  if dir == 0:     # 왼쪽으로 회전의 경우 앞의 숫자들을 계속 맨 뒤로 보내는 것임.
    # store = num[row][:cnt]
    # del num[row][:cnt]
    # num[row] += store 이렇게 길게 풀지 않고 pop을 이용해 한 줄로 적어줄 수 있음.
    for _ in range(cnt):     # cnt(움직이는 개수)만큼만 반복문이 돌아야 하는 것 기억!
      num[row].append(num[row].pop(0))
  else:      # 오른쪽으로 회전의 경우 뒤의 숫자들을 계속 맨 앞으로 가지고 나오는 것임.
    for _ in range(cnt):
      num[row].insert(0, num[row].pop())     # pop()은 어차피 맨 뒤의 1개의 수를 꺼내오기 때문에 -1을 인자로 적을 필요가 없다.

# 모래시계 모양 영역 감의 개수 출력
r = N - 1     # (N은 길이를 나타내므로) 이렇게 해야 인덱스가 정상적으로 됨.
l = 0
res = 0
for i in range(N):
  for j in range(l, r + 1):
    res += num[i][j]
  if i < N // 2:
    l += 1
    r -= 1
  else:
    l -= 1
    r += 1
print(res)