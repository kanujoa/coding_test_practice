'''
변수명 정하기
 1) 영문과 숫자, _로 이루어진다.
 2) 대소문자를 구분한다.
 3) 문자나, _로 시작한다.
 4) 특수문자를 사용하면 안된다. (&, % 등)
 5) 키워드를 사용하면 안된다. (if, for 등)
'''

a = 1
A = 2
A1 = 3
#2b = 4
print(a, A, A1)
a, b, c = 3, 2, 1
print(a, b, c)

#값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 1234567823424453535
print(type(a))
print(a)
a = 12.123456789123456789     # float는 8바이트까지만 출력됨.
print(a)
a = 'student'
print(a)
print(type(a))

#출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='')
print(a, b, c, sep='\n')
print(a, end=' ')     # 1 출력되고 옆으로 한칸
print(b, end=' ')     # 2 출력되고 옆으로 한칸
print(c)     # 옆에 바로 3 출력 (1 2 3 이렇게 한줄로 출력)
