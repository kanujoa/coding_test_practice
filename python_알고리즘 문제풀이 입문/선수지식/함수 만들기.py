'''
함수 만들기
'''
'''
def add(a, b):
    c = a + b
    print(c)

add(3, 2)     함수를 만든 후 호출해야 한다.
add(5, 7)
'''
'''
def add(a, b):
    c = a+b
    return c

x = add(3, 2)     # 옆의 함수 자제가 return된 값을 가짐.
print(x)     
'''
'''
def add(a, b):
    c = a + b
    d = a - b
    return c, d      # 여러 개의 값을 return시킬 수도 있다.

print(add(3, 2))
'''

# 소수만 출력시키기
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):     # True일 때만 아래 실행문 실행함.
        print(y, end=' ')

