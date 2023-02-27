N = int(input())

# 문제에 그려져 있는 대로 격자판 완성
grating = [list(map(int, input().split())) for _ in range(N)]     # 우선 사용자의 입력을 받아 격자판 만들기 (N * N)
grating.insert(0, [0] * (N + 2))     # 맨 위 행에 0으로만 된 줄 추가
grating.append([0] * (N + 2))     # 맨 아래 행에 0으로만 된 줄 추가
for i in grating:     # 각 행의 맨 앞 격자와 맨 끝 격자에 0 추가
  i.insert(0, 0)
  i.append(0)


# 격자판 상하좌우 숫자 크기 비교
cnt = 0     # 봉우리 개수를 나타내는 변수 cnt
for r in range(1, N+1):     # 봉우리는 사용자 입력에서만 찾으면 되므로 탐색할 행의 범위는 1부터 N까지
  for c in range(1, N+1):     # 열의 범위도 마찬가지
    cur = grating[r][c]     # 현재 격자
    if cur > grating[r-1][c] and cur > grating[r+1][c]  and cur > grating[r][c-1] and cur > grating[r][c+1]:
      cnt += 1     # 현재 격자가 나타내는 숫자가 (순서대로)상하좌우 숫자들보다 크면 cnt 1 증가 (조건을 모두 만족해야 하므로 and 사용)
print(cnt)