# 최대 힙은 부모 노드의 값이 항상 자식 노드의 값보다 커야 한다. (최소 힙과 반대!)

import heapq as hq     # heapq는 항상 최소힙 기준으로 작동한다. 따라서 값을 넣을 때 -부호를 붙여(부호를 반대로 하여) 넣고, 최소힙 코드를 적용해 주면 최대힙을 구현할 수 있다.
a = []

while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))      # 출력시 - 붙여 원래 부호로 만들기
    else:
        hq.heappush(a, -num)     # - 붙여서 부호 바꾸어 집어넣기