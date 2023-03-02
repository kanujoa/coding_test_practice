# 숫자의 존재 여부를 체크하는 ch list 총 3개 필요! (행, 열, 그룹), 함수를 이용해 코드 작성!
# 2차원 리스트의 인덱스값을 ch 리스트의 인덱스로 하여 해당 부분의 값이 1이 되게 하여 체크함. (누적이 아님. 1로 변환시키는 것임. 똑같은 숫자가 나와도 해당 부분의 값은 계속 1)
# ch 리스트의 원소들을 sum 하여 sum 값이 9면 나오지 않은 숫자가 없는 것이므로 올바른 스도쿠이고, 9가 아니면 틀린 스도쿠이다.

def check(a):      # 여기서의 a는 check 함수의 지역변수이므로 문제 없다.
  # 행, 열 탐색 (2중 for문 이용)
  for i in range(9):
    ch1 = [0] * 10     # 행 숫자 탐색 리스트 생성 (1부터 9까지의 숫자를 체크할 것이므로 인덱스는 편하게 10까지로 생성, 값은 모두 0으로 초기화함.)
    ch2 = [0] * 10     # 열 숫자 탐색 리스트 생성
    for j in range(9):
      ch1[a[i][j]] = 1     
      ch2[a[j][i]] = 1
    if sum(ch1) != 9 or sum(ch2) != 9:     # 겹치는 숫자가 있는 리스트가 있는지 탐색
      return False     # return을 하게 되면 함수가 종료되는 것이므로 아래의 코드가 실행되지 않게 된다.
  # 그룹 탐색 (4중 for문 이용)
  for i in range(3):     # 그룹 (3 * 3) 탐색 (총 9번을 돌고, 후에 곱하기를 이용하여 range(3)에 해당하는 숫자들을 바꾸어줄 것이다.)
    for j in range(3):
      ch3 = [0] * 10     # 그룹 숫자 탐색 리스트 생성
      for k in range(3):     # 그룹 안의 숫자 탐색
        for s in range(3):
          ch3[a[i*3+k][j*3+s]] = 1     # 그룹 안에서 왼쪽에서 오른쪽으로, 위에서 아래로 숫자 탐색
      if sum(ch3) != 9:
        return False     
  return True     # 위의 for문들을 return 없이 그냥 통과했을 때 True를 return한다.

a = [list(map(int, input().split())) for _ in range(9)]     # 입력 받기 ([] 안에 코드를 작성하여 2차원 리스트로 만들기)
if check(a):     # check 함수에 a를 인자로 넣어 반환된 값이 True이면
  print("YES")     # YES 출력
else:     # 반환된 값이 False이면
  print("NO")     # NO 출력