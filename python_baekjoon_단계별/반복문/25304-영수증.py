x = int(input())     # 총 금액
n = int(input())     # 구매한 물건의 종류의 수

t = 0     # 영수증에서의 총 금액
for _ in range(n):
  a, b = map(int, input().split())
  t += a * b

if t == x:
  print("Yes")
else:
  print("No")
