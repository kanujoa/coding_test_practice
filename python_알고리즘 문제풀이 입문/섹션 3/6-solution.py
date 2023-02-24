# 격자판을 그리고 위쪽과 왼쪽에 인덱스를 매겨 확인하기
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]     # 2차원 리스트 한번에 작성하기 --> 리스트 컴프리헨션 (map 함수가 1줄을 읽어서 list 함수가 리스트화시킴, 변수는 없는 것으로 작성하여 저장 시간 없애기)
# for x in a:     --> 보기 좋게 한 줄에 하나의 리스트가 출력됨.
#   print(x)      
largest = -2147000000     # 최댓값을 찾는 것이므로 가장 작은 값으로 초기화
for i in range(n):     # i는 가로부분의 인덱스에 해당
  sum1 = sum2 = 0    # 행의 합 sum1, 열의 합 sum2
  for j in range(n):     # j는 세로부분의 인덱스에 해당 (j가 다 돌아야 i가 하나 추가됨)
    sum1 += a[i][j]     # 행이 고정되고 각 열을 탐색
    sum2 += a[j][i]     # 열이 고정되고 각 행을 탐색
  if sum1 > largest:     # sum1이 largest보다 클 경우 largest가 sum1으로 바뀜.
    largest = sum1
  if sum2 > largest:     # sum2가 largest보다 클 경우 largest가 sum2로 바뀜. (elif가 아닌 if이므로 위의 if문 실행 이후에도 반드시 거쳐짐.)
    largest = sum2

sum1 = sum2 = 0     # 오른쪽 아래로 내려가는 대각선은 sum1, 왼쪽 아래로 내려가는 대각선은 sum2
for i in range(n):
  sum1 += a[i][i]     # [i][i]가 되는 이유는 대각선은 인덱스 번호가 같기 때문이다.
  sum2 += a[i][n-i-1]
if sum1 > largest:     # 다시 largest 업데이트 (sum1 또는 sum2가 앞에서 largest에 저장된 수보다 더 클 때)
  largest = sum1
if sum2 > largest:
  largest = sum2

print(largest)