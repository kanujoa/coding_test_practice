# 딕셔너리라는 파이썬에 있는 자료구조를 사용하면 편하게 풀 수 있다.
# list의 index는 정수값만 되지만 dictionary의 key값은 문자, 숫자 모두 가능하다.
# 노트에 적어놓을 단어들을 key 값으로 하고, value는 모두 0으로 초기화해 dictionary를 만든다. 
# 시에 적어놓은 단어들이 나올 때마다 그 단어와 일치하는 key의 value를 0으로 바꾼다.
# 마지막에 value가 1인 key값을 출력해 주면 된다.

n = int(input())
p = dict()     # 빈 딕셔너리 p 만들기
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] = 0     # 없는 단어의 경우(key값이 없을 경우) 딕셔너리의 변화 없이 그냥 넘어가게 된다.
for key, val in p.items():     # dic_name.items()는 dic의 각 요소의 key와 value를 쌍으로 반환해줌. 옆에서는 key와 val 변수에 각각 key값과 value값이 대입됨.
    if val == 1:
        print(key)    