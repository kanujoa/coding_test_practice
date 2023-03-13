# 키 큰 순서대로 정렬해서 자신보다 이전 인덱스에 있는 모든 선수들하고 몸무게를 비교하여 더 적게 나가는 경우가 있으면 탈락, 모든 경우에서 더 많이 나가면 진출
# 키는 이미 큰 순서대로 정렬되어 있으므로 볼 필요 X, 몸무게만 본다.
# 2중 for문은 비효율적! 몸무게의 최댓값을 구해간다고 생각하고 코드를 짜는 것이 좋음!

import sys
input = sys.stdin.readline
n = int(input())
body = []
for i in range(n):
  a, b = map(int, input().split())
  body.append((a, b))     # 키와 몸무게를 튜플 형태로 묶어서 저장
body.sort(reverse=True)     # 내림차순 정렬
largest = 0     # 몸무게의 최댓값
cnt = 0     # 출전 가능 선수의 수
for x, y in body:     # x = 키, y = 몸무게
  if y > largest:     # 몸무게가 largest에 저장된 값보다 큰 경우
    largest = y     # largest는 y로 초기화
    cnt += 1     # cnt도 증가
print(cnt)