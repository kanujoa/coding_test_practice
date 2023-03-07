import sys
input = sys.stdin.readline
n, m = map(int, input().split())     # n: 바구니의 번호 개수, m: 공을 넣을 횟수
basket = [0 for _ in range(n+1)]     # [0] * n 으로 작성하는 것이 더 편함.
for _ in range(m):
  i, j, k = map(int, input().split())     # i번 바구니부터 j번 바구니까지 k번 번호가 적혀져 있는 공을 넣는다. (각 번호의 공은 매우 많음.)
  for idx in range(i, j+1):
    basket[idx] = k
basket.pop(0)
for a in basket:
  print(a, end=" ")