'''
변수입력과 연산자


a = input("숫자를 입력하세요 : ")
print(a)

a, b = input("숫자를 입력하세요 : ").split()     # a, b는 string, split()은 띄어쓰기로 입력 의미
print(type(a))
c = a + b
print(type(c))
print(c)

a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(a + b)

a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)     # 몫
print(a % b)
print(a ** b)     # 거듭제곱
'''

a = 4.3
b = 5
c = a + b     # 실수형과 정수형을 연산하면 결과는 실수형이다.
print(type(c))
print(c)
