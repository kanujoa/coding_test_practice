n = int(input())     # 주어지는 명령의 수
commands = [input() for _ in range(n)]     # 주어지는 명령들
stack = []

for command in commands:
    if 'push' in command:
        stack.append(command.split()[-1])
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())