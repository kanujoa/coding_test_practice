# 모든 환자의 응급도가 다 다른 것은 아니다. 응급도가 같은 환자가 있을 수 있으므로 환자별로 번호를 붙여주어야 했다.
# (enumerate를 사용함.)

from collections import deque
n, m = map(int, input().split())
degree = deque(list(enumerate(map(int, input().split()))))
priority = max(d[1] for d in degree)
cnt = 0
while degree:
    if degree[0][1] != priority:     # 환자가 우선 순위 환자가 아니면
        degree.append(degree.popleft())
    else:     # 환자가 우선 순위이면
        if degree[0][0] == m:     # 우선 순위이면서 m번째로 지정된 환자이면
            cnt += 1
            print(cnt)
            break
        else:     # m번째 환자가 아니면
            degree.popleft()
            cnt += 1
            priority = max(d[1] for d in degree)