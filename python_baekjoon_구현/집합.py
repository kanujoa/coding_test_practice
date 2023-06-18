# 이렇게 작성하면 시간초과 난다..
import sys
input = sys.stdin.readline

_set = set()      # 비어 있는 집합 생성

m = int(input())     # 주어지는 명령의 수

for _ in range(m):
    command = input().split()     # 명령 한줄씩 입력받기
    if 'all' in command:     # 명령이 all이면
        _set = {str(i) for i in range(1, 21)}     # _set을 1부터 20까지의 원소가 있는 집합으로 바꾼다.
    elif 'empty' in command:     # 명령이 empty이면
        _set.clear()     # _set을 공집합으로 만든다.  
    elif 'add' in command:     # 명령에 add라는 글자가 있을 경우
        _set.add(command[1])     # 공백을 기준으로 명령을 나눈 뒤 인덱스 1의 요소를 _set 집합에 추가한다.
    elif 'check' in command:     # 명령에 check라는 글자가 있을 경우
        if command[1] in _set:      # command[1]이 _set 집합에 존재할 경우 1, 존재하지 않을 경우 0을 출력한다.
            print(1)  
        else:
            print(0)   
    elif 'remove' in command and command[1] in _set:     # 명령에 remove라는 글자가 있고 동시에 command[1]이 _set의 원소로 존재할 경우
        _set.remove(command[1])     # 그 command[1]을 삭제 (command[1]이 _set에 존재하지 않는데 삭제하려 하면 keyError가 발생한다.)
    elif 'toggle' in command:      # 명령에 toggle이라는 글자가 있을 경우
        if command[1] in _set:     # command[1]이 _set에 있을 경우
            _set.remove(command[1])     # _set에서 command[1] 삭제
        else:     # command[1]이 _set에 존재하지 않을 경우
            _set.add(command[1])     # _set에 command[1] 추가


# 통과되는 풀이
import sys
input = sys.stdin.readline
m = int(input())

s = set()
for _ in range(m):
    command = input().rstrip('\n')
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