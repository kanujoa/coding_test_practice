# 사용자 입력을 받아 스도쿠 만들기
sudoku = [list(map(int, input().split())) for _ in range(9)]

# 행과 열을 탐색하여 1부터 9까지의 숫자 중 겹치는 숫자가 없는지를 확인

for a in range(9):
  row = []
  column = []
  for b in range(9):
    row.append(sudoku[a][b])
    column.append(sudoku[b][a])
  for num in range(1, 10):
    if row.count(num) > 1 or column.count(num) > 1:
      print("NO")
      break
else:     # 박스(3 * 3)를 탐색하여 1부터 9까지의 숫자 중 겹치는 숫자가 없는지를 확인
  i = 0
  for c in range(i, i+3):     # 행에 해당
    box = []
    for d in range(i, i+3):     # 열에 해당
      box.append(sudoku[c][d])
    for num in range(1, 10):
      if box.count(num) > 1:
        print("NO")
        break
    i += 3
  else:
    print("YES")