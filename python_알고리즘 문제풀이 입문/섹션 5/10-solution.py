# 최소힙은 완전이진트리로 구현된 자료구조임.
# 트리에서 동그란 부분을 노드, 이어주는 선을 간선이라 함.
# 맨 위의 노드는 root 노드라고 하고, 그 노드가 1번이고, 그 노드의 왼쪽 자식은 2번, 오른쪽 자식은 3번임.
# 부모, 왼쪽 자식, 오른쪽 자식이 트리의 기본 구성 요소이고, 그 묶음이 하나의 트리가 됨.
# 자식이 트리로 구성되어 있다면 root 노드의 왼쪽 서브트리, root 노드의 오른쪽 서브트리라고 부른다.
# root 노드부터 아래쪽으로 갈수록 레벨이 높아짐, 같은 라인이면 같은 레벨
# 부모의 노드 값은 두 자식(왼쪽, 오른쪽)의 노드값보다 무조건 작아야 함. 부모가 자식보다 큰 경우가 있으면 swap해야 함. 이때, root node까지 모두 비교해 보아야 함.(upheap)
# 0이 입력되면 root node의 값(최상위 부모의 값)이 pop되어 출력되는데, 이때 가장 아래, 가장 오른쪽 자식이 root node에 들어가게 되고 최소힙을 만드는 과정을 거친다.(downheap)

import heapq as hq     # python에서는 heapq 모듈을 이용해 heap을 구현할 수 있다.
a = []     # python 힙을 구현하기 위해 리스트가 필요함. (heappush 함수와 heappop 함수를 이용하면 리스트가 힙 자료구조처럼 동작이 된다.)
while True:
    n = int(input())
    if n == -1:
        break 
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))      # hq.heapop(리스트명)
    else:
        hq.heappush(a, n)     # hq.heappush(리스트, 추가할 요소)

# 최소힙 만드는 과정 그려보기!