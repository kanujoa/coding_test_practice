import sys
input = sys.stdin.readline

def Count(len):     # mid(가장 가까운 두 말의 거리)에 따라 배치할 수 있는 말의 수
  cnt = 1     # 말 한마리를 먼저 배치하고 시작
  ep = Line[0]     # 마지막 말을 배치한 지점 (end point, 처음에는 0부터 시작)
  for i in range(1, n):
    if Line[i] - ep >= len:
      cnt += 1
      ep = Line[i]
  return cnt

n, c = map(int, input().split())
Line = [int(input()) for _ in range(n)]
Line.sort()     # 항상 오름차순으로 입력되는 것이 아니므로 Line 리스트를 오름차순 정렬해 주어야 한다.
lt = 1     # 최소 거리(마구간의 맨 앞 좌표)
rt = Line[n-1]     # 최대 거리(마구간의 맨 끝좌표)

while lt <= rt:
  mid = (lt + rt) // 2     # mid를 가장 가까운 두 말의 거리라고 가정해 놓고 그게 맞는지를 확인한다.
# 따라서 마구간의 거리가 mid보다 작은 경우에는 그 곳에 말을 배치할 수 없다. 마구간의 거리가 mid 보다 크거나 같을 때만 배치 가능하다.
  if Count(mid) >= c:     # 놓을 수 있는 말의 수가 입력에서 주어진 수보다 크거나 같으면
    res = mid     # 일단 결과는 mid
    lt = mid + 1     # '최대' 거리를 찾아야 하므로 lt를 mid 바로 옆으로 옮긴다.
  else:      # 놓을 수 있는 말의 수가 입력에서 주어진 수보다 작으면
    rt = mid - 1     # 거리가 너무 큰 것이므로 거리를 좁혀주기 위해 rt를 mid 바로 앞으로 옮긴다.

print(res)