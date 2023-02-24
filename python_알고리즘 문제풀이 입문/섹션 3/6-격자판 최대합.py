N = int(input())
grating = []     # 이차원 리스트가 될 것임.
for i in range(N):
  grating.append(list(map(int, input().split())))

# 각 행의 합
row = []
for i in range(len(grating)):
  total = 0     # 변수명을 함수명 같은 것으로 하면 (ex) sum) 후에 typeerror가 날 수 있음.
  for line in grating:
    total += line[i]
  row.append(total)
row = max(row)     # 각 행 합 중 가장 큰 값

# 각 열의 합
column = []
for line in grating:
  column.append(sum(line))
column = max(column)     # 각 열 합 중 가장 큰 값

# 각 대각선의 합
right = 0     # 오른쪽 아래로 내려가는 대각선 합
left = 0     # 왼쪽 아래로 내려가는 대각선 합
i = 0
for line in grating:
  right += line[i]
  left += line[-i-1]
  i += 1
diagonal = max([right, left])     # 오른쪽, 왼쪽 대각선 합 중 더 큰 값

print(max([row, column, diagonal]))     # 행, 열, 대각선 합 중 가장 큰 것을 출력하기