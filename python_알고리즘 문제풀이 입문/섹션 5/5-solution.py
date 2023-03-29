# 큐 : 어떤 데이터를 '큐'라는 자료구조에 넣을 때에는 뒤쪽부터 넣고 꺼낼 때는 앞쪽에서 꺼낸다. 즉, 들어가는 순서대로 나온다.
# --> First In First Out (선입선출, FIFO), 들어가는 입구가 있고 나가는 출구가 있으므로 뚫려 있는 곳이 2개!
# 스택에서는 한 곳으로 들어가고 나오므로 후입선출(LIFO)이었다.
# python에서는 deque라는 자료구조를 지원하는데, 그것에서 지원하는 함수인 popleft()와 append()를 활용하여 문제를 해결하면 된다.

from collections import deque
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)     # 리스트 dq를 deque 자료구조로 만들기 (deque() 이용)
while dq:     # dq가 비어 있을 때 멈추기
    for _ in range(k-1):     # k-1번 돌기 (k번째 이전 순서까지 아래의 코드 실행)
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()     # for문을 벗어났다는 것은 k번째 왕자라는 의미이므로 dq에서 삭제
    if len(dq) == 1:     # 만약 dq의 길이가 1이라면 왕자 한 명만 남은 것이므로
        print(dq[0])     # 그 왕자의 번호 출력
        dq.popleft()     # 마지막 왕자를 없애면 dq가 비게 되므로 while문 자동 종료