grating = [list(map(int, input().split())) for _ in range(7)]

cnt = 0     # 회문수 세기

# 가로, 세로 한꺼번에 탐색 : 왼쪽에서 오른쪽으로 5개의 숫자를 row 리스트에 담아 가로로 탐색, 위쪽에서 아래쪽으로 5개의 숫자를 column 리스트에 담아 세로로 탐색
# (가로 탐색 시 위에서부터 아래로 탐색, 모든 행을 다 돌면 다시 위로 올라옴. 세로 탐색 시 왼쪽에서부터 오른쪽으로 탐색, 모든 열을 다 돌면 다시 왼쪽으로 돌아옴.)
for a in range(3):     # 열의 인덱스 시작지점을 나타냄.
  for b in range(7):     # 행 index
    row = []
    column = []
    for c in range(a, a+5):     # 열 index
      row.append(grating[b][c])
      column.append(grating[c][b])
    for i in range(2):
      if row[i] != row[-1-i]:     # row 리스트 회문인지 아닌지 여부 결정 (회문이 아닐 경우)
        break     # 반복문 빠져나감 (카운트하지 않음.)
    else:     # for문 break 걸리지 않고 그냥 빠져나갈 경우 (회문일 경우)
      cnt += 1     # cnt에 1 추가
    for i in range(2):     # column 리스트도 마찬가지
      if column[i] != column[-1-i]:
        break
    else:
      cnt += 1

print(cnt)