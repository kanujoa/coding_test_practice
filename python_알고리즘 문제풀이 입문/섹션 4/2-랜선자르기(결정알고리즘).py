import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]     # 랜선의 길이를 한 줄씩 입력받아 lan 리스트에 넣기

lt = 0     # 왼쪽값 0으로 초기 설정
rt = max(lans)     # 오른쪽 값 lans 리스트에서 가장 큰 값으로 값으로 초기 설정
res = 0

while lt <= rt:     # lt가 rt보다 작거나 같다는 것은 이분 탐색이 가능하다는 의미임.
  mid = (lt + rt) // 2     # mid는 계속 바뀌므로 while문 안에 넣어줌. mid는 항상 lt와 rt 사이에서의 중간값!
  s = 0     # 잘라서 나오는 랜선의 개수를 합한 값을 나타내는 변수 정의
  for lan in lans:     # lans 리스트의 요소들 하나하나 탐색
    s += lan // mid     # s에 각 랜선의 길이를 mid로 나눈 몫을 더함 (그 몫은 잘라서 나올 수 있는 길이가 mid인 랜선의 개수임)
  if s >= N:     # 잘라서 나온 랜선의 개수인 s가 필요한 랜선의 개수인 N과 같거나 큰 경우 (문제에서 렌선을 자를 때 손실되는 길이는 없다고 가정하므로 큰 것도 포함한다.)
    if mid > res:     
      res = mid     # 일단 결과는 mid (끝까지 돈 다음 가장 큰 mid값이 답이 됨.)
      lt = mid + 1     # s == N인 더 큰 mid가 있는지 살펴보아야 하므로 lt를 mid 바로 옆으로 옮겨줌.
  elif s < N:     # s가 N보다 작으면 필요한 개수보다 적다는 뜻이므로 길이를 더 짧게 잘라서 개수를 늘려야 한다.
    rt = mid - 1     # 따라서 mid가 작아져야 하므로 rt가 mid 바로 앞으로 이동

print(res)

# 여기서만 그치면 많은 케이스를 통과하지 못한다. 여기서는 s == N이 참이 되자마자 그에 해당하는 mid를 print하고 바로 프로그램이 종료
# 되는데, 그 값보다 더 큰 값들 중에서도 답이 나올 수 있는지도 확인해 보아야 한다. 몫만 보는 것이기 때문에 s == N이 되게 만드는 mid가
# 여러개일 수 있다.     --> 따라서 res를 추가해줌.