import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    command = input().strip('\n')     # 개행 문자가 포함되어 있으므로 이것을 제거해야지 런타임 에러가 나지 않고 아래 조건문 중 하나 실행 가능!
    if 'push_back' in command:
        d.append(command.split()[1])
    elif 'push_front' in command:
        d.appendleft(command.split()[1])
    elif command == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif command == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
    elif command == 'size':
        print(len(d))
    elif command == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif command == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif command == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())