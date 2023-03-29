# k번째 왕자가 제외되어야 한다는 의미이다. k번째 왕자가 한 번 제외되었다면 k번째 왕자를 제외한 n-1명의 왕자들 중 다시 
# k번째 왕자를 제외시킨다. 시계방향으로 돌아가므로 자신의 번호를 외치고 나간 k번째가 아닌 왕자들은 리스트의 뒤로 가야 한다.
# 이 과정을 왕자 1명만 남을 때까지 반복한다.

from collections import deque     # python에서 큐는 deque를 import 시켜서 구현함.
n, k = map(int, input().split())
dq = deque(i+1 for i in range(n))
cnt = 1
while len(dq) != 1:
    if cnt == k:
        dq.popleft()
        cnt = 1
    else:
        dq.append(dq.popleft())
        cnt += 1
print(dq[0])