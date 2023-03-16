# 자료구조 데크(deque) 이용하여 해결하기
from collections import deque      # 모듈 불러오기
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)     # 정렬된 리스트를 deque 함수 안에 넣음
cnt = 0
while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()     # 맨 마지막 자료를 꺼낼 땐 똑같이 pop() 사용
        cnt += 1
    else:
        p.popleft()     # 맨 첫번째 자료를 꺼낼 땐 pop(0) 대신 popleft() 사용
        p.pop()
        cnt += 1
print(cnt)