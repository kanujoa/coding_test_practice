n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0

s = e = n // 2     # s는 오른쪽 부분, e는 왼쪽 부분에 해당하게 될 인덱스임.
for i in range(n):     # i는 행에 해당하게 될 것
  for j in range(s, e+1):     # j는 열에 해당하게 될 것
    res += a[i][j]     # 인덱스가 s 이상 e+1의 범위를 다 돌때까지 res에 a 이차원 리스트의 i행 j열 값이 계속 더해진다.
  if i < n // 2:     # 가운데 줄보다 윗줄일 경우
    s -= 1     # s는 1 감소
    e += 1     # e는 1 증가하여 더하는 범위 늘림
  else:     # 가운데 줄이랑 그 아랫줄일 경우
    s += 1     # s는 1 증가
    e -= 1     # e는 1 감소하여 더하는 범위를 좁혀감
print(res)