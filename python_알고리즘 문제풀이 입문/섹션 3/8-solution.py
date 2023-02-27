n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 회전명령 수행
for i in range(m):     # 명령 부분은 입력을 받으면서 변수에 저장해 주는 것이 좋다.
  h, t, k = map(int, input().split())     # h는 행, t는 방향, k는 개수
  if t == 0:     # 왼쪽 방향으로 회전
    for _ in range(k):     # k번만큼 회전 반복
      a[h-1].append(a[h-1].pop(0))     # h행에 해당하는 0번 인덱스값을 빼내어 삭제하고 그것을 append(제일 앞의 자료가 맨 뒤에 추가됨.)
  else:     # 오른쪽 방향으로 회전일 경우
    for _ in range(k):
      a[h-1].insert(0, a[h-1].pop())     # h행에 해당하는 끝 요소를 pop후 a[h-1] 리스트의 0번 인덱스에 삽입

# 모래시계 모양 영역의 감의 개수 출력
res = 0
s = 0     # s는 왼쪽 부분
e = n - 1     # e는 오른쪽 부분
for i in range(n):     # i는 행을 나타냄  
  for j in range(s, e+1):     # j는 열을 나타냄 (s 이상 e 이하)
    res += a[i][j]     # j의 범위만큼 a[i][j]에 위치한 숫자를 더함.
  if i < n // 2:     # i가 맨 가운데줄에 해당하는 n // 2보다 작으면
    s += 1     # s의 숫자를 늘리고
    e -= 1     # e의 숫자를 줄여서 좁혀나감
  else:     # i가 맨 가운데줄에 해당하는 n // 2랑 같거나 더 크면
    s -= 1     # s의 숫자를 줄이고
    e += 1     # e의 숫자를 늘려서 넓혀나감
print(res)

