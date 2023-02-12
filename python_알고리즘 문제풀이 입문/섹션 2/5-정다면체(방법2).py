N, M = map(int, input().split())

cnt = [0 for i in range(N+M+1)]     # 인덱스 리스트 생성 (초깃값은 모두 0으로 함. 후에 더한 값과 같은 인덱스 값 부분에 카운트를 추가해줌.)

for n in range(1, N+1):
  for m in range(1, M+1):
    cnt[m+n] += 1

max_count = max(cnt)
for idx, count in enumerate(cnt):
  if max_count == count:
    print(idx, end=" ")