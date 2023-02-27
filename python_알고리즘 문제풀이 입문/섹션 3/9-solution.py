n = int(input())

# 상하좌우 좌표 활용을 위해 정의 (차례대로 적용하면 12시, 3시, 6시, 9시 방향이 됨.)
dx = [-1, 0, 1, 0]      # 행  
dy = [0, 1, 0, -1]     # 열

# 문제에 그려져 있는 대로 격자판 완성
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
  x.insert(0, 0)
  x.append(0)

# 격자판 상하좌우 숫자 크기 비교해서 봉우리 개수 구하기
cnt = 0
for i in range(1, n+1):
  for j in range(1, n+1):
    if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):      # 위 dx, dy 리스트 활용
      cnt += 1
print(cnt)
# all 함수: all 함수에 인자로 들어가는 조건이 모두 참일 때만 true를 반환함.
# 내가 and를 이용해 작성한 방법보다 훨씬 더 코드가 짧아진다.