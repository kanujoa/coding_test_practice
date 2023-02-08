'''
반복문(for, while)
'''
'''
a = range(1, 11)     # range: 순차적으로 정수 리스트를 만드는 함수
print(list(a))
'''
'''
for i in range(10, 0 , -2):
    print(i)
'''
'''
i = 1
while i <= 10:
    print(i)
    i = i + 1
'''
'''
i = 10
while i >= 1:
    print(i)
    i = i - 1
'''
'''
i = 1
while True:
    print(i)
    if i == 10:
        break
    i += 1
'''
'''
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
'''
'''
for i in range(1, 11):
    print(i)
    if i == 5:
        break
else:     # 위에서 break가 걸리면 else문은 실행되지 않는다.
    print(11)
'''

for i in range(1, 11):
    print(i)
    if i > 15: 
        break     # 이 경우처럼 break가 걸리지 않고 for문이 종료되면 아래 else문 실행됨.
else:
    print(11)
