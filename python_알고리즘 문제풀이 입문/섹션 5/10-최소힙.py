from collections import deque
import sys
input = sys.stdin.readline

heap = deque()
while True:
    num = int(input())
    if num == -1:
        break
    elif num != 0:
        for i in range(len(heap)):
            if heap[i] > num:
                if i != 0:
                    heap.insert(i, num)
                else:
                    heap.insert(0, num)
                break
        else:
            heap.append(num)
    else:
        if len(heap) == 0:
            print(-1)
        else:
            print(heap.popleft())