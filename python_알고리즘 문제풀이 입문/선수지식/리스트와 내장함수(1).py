'''
리스트와 내장함수(1)
'''

import random as r
a=[]     # 빈 리스트
# print(a)
b = list()     # 빈 리스트
#print(b)

a = [1, 2, 3, 4, 5]
# print(a)
# print(a[0])

b = list(range(1, 11))
# print(b)

c = a + b
# print(c)

print(a)
a.append(6)
print(a)

a.insert(3, 7)     # a리스트의 3번 인덱스에 7이 들어간다. (원래 3번 인덱스 이상의 원소들은 뒤로 밀려남.) 
print(a)

a.pop()     # 맨 뒤 요소를 리스트에서 제거
print(a)
a.pop(3)     # a 리스트의 3번 인덱스를 제거
print(a)

a.remove(4)     # a 리스트에서 4 지우기
print(a)

print(a.index(5))     # a 리스트에서 5를 찾아서 그것의 인덱스 알려줌.

a = list(range(1, 11))
print(a)
print(sum(a))     # a 리스트의 원소들을 모두 합친 값
print(max(a))     # a 리스트에서 가장 큰 값을 찾아줌.
print(min(a))     # a 리스트에서 가장 작은 값을 찾아줌.
print(min(7, 5))     # 7, 5 중 가장 작은 값을 찾아줌.
print(min(7, 3, 5))     # 7, 3, 5 중 가장 작은 값을 찾아줌.
print(a)
r.shuffle(a)     # shuffle: a 리스트를 섞는 메서드
print(a)
a.sort(reverse=True)     # a 리스트를 내림차순으로 정렬
print(a)
a.sort()     # a 리스트를 오름차순으로 정렬
print(a)

a.clear()     # a 리스트의 원소들을 모두 지운다.
print(a)
