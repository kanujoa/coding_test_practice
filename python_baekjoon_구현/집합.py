import sys
input = sys.stdin.readline
m = int(input())

s = set()
for _ in range(m):
    command = input().rstrip('\n')     # sys.stdin.readline은 개행 문자를 그대로 돌려주기 때문에 끝에 붙어 있는 개행 문자를 제거해 주어야 한다.
    if 'add' in command:
        if int(command.split()[1]) not in s:
            s.add(int(command.split()[1]))
    elif 'check' in command:
        if int(command.split()[1]) in s:
            print(1)
        else:
            print(0)
    elif 'remove' in command:
        if int(command.split()[1]) in s:
            s.remove(int(command.split()[1]))
    elif 'toggle' in command:
        if int(command.split()[1]) in s:
            s.remove(int(command.split()[1]))
        else:
            s.add(int(command.split()[1]))
    elif command == 'all':
        s = set(list(i for i in range(1, 21)))
    elif command == 'empty':
        s.clear()