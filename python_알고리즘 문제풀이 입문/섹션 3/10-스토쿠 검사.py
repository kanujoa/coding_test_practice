# 사용자 입력을 받아 스도쿠 만들기
sudoku = [list(map(int, input().split())) for _ in range(9)]
play = True     # play가 False가 될 때 가장 바깥쪽 for문을 멈추게 하기 위해 설정 (문제가 없을 때는 정상적으로 돌아야 하므로 기본값을 true로 설정)

# 행과 열을 탐색하여 겹치는 숫자가 있는지를 확인
for r in range(9):     # 행을 나타낼 인덱스
  if play == False:     # play가 False로 바뀌면
    break     # 가장 바깥쪽 반복문을 빠져나간다.
  row = []     # 한 행의 숫자들을 담을 리스트
  column = []     # 한 열의 숫자들을 담을 리스트
  for c in range(9):     # 열을 나타낼 인덱스
    row.append(sudoku[r][c])     # 한 행에 해당하는 숫자들을 row 리스트에 추가시키기 (첫번째 인덱스 고정, 두번째 인덱스가 바뀜.)
    column.append(sudoku[c][r])     # 한 열에 해당하는 숫자들을 column 리스트에 추가시키기 (첫번째 인덱스가 바뀌고 두번째 인덱스는 고정.)
  for n in range(1, 10):     # 겹치는 숫자가 있는지를 탐색할 것이므로 n(숫자)의 범위 1부터 10까지로 설정
    if row.count(n) > 1 or column.count(n) > 1:     # 각 리스트에서 숫자 n이 2개 이상 있으면 올바른 스도쿠가 아니므로
      print("NO")     # NO 출력 후
      play = False     # play를 멈추어야 하므로 play에 False 할당
      break     # 현재 반복문 빠져나가기
else:     # 위의 for문들을 break 없이 빠져나가면 box(3 * 3)를 탐색하여 겹치는 숫자가 있는지를 확인
  a = 0     # r 범위의 시작으로 이용할 숫자
  b = 0     # c 범위의 시작으로 이용할 숫자
  while play:     # play가 True일 때까지만 반복
    if a == 9:     # 만약 i가 9가 되는 순간이 온다면 모든 box를 다 돌아봤는데 겹치는 숫자가 없는 것이므로
      print("YES")     # YES 출력 후
      break     # 가장 바깥쪽 반복문 빠져나가기
    box = []      # 한 box의 숫자를 담을 리스트 생성
    for r in range(a, a+3):     # r은 행 의미, 범위는 3개의 숫자
      for c in range(b, b+3):     # c는 열 의미, 범위는 3개의 숫자   
        box.append(sudoku[r][c])     # box 리스트에 3*3의 범위에 해당하는 숫자를 넣기
    for n in range(1, 10):     # 1부터 9까지의 수 중 겹치는 숫자가 있는지 확인하기
      if box.count(n) > 1:     # 겹치는 수가 있으면
        print("NO")     # NO 출력 후
        play = False     # play 중단을 위해 False 할당
        break     # 현재 반복문 빠져나가기
    if b == 6:     # b가 6이 되면 3 * 9 부분을 다 돈 것이므로
      a += 3     # a에 3을 더해 3칸 아래쪽으로 이동
      b = 0     # b는 다시 맨 왼쪽에서부터 시작
    b += 3     # 하나의 box 탐색을 마치면 b에 3 더해주기