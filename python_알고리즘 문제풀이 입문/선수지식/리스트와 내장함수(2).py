'''
리스트와 내장함수(2)
'''

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:     # 위 아래 모두 똑같은 결과
    print(x, end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

for x in enumerate(a):     # enumerate를 사용하면 튜플 형태로 각 인덱스에 해당하는 a리스트의 원소가 서로 짝지어져서 나옴.
    print(x)

b=(1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7     # 튜플 값은 리스트와 다르게 절대 변경 불가!

b = [1, 2, 3, 4, 5]
b[0] = 7
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])     # 튜플 형태로 묶여서 나오는 것이 아니라 값만 나오게 할 수 있음.
print()

for index, value in enumerate(a):     # 위의 코드와 동일
    print(index, value)
print()

if all(60 > x for x in a):     # 조건에서 하나라도 거짓이 되면 false return(boolean 형태로 답이 나옴.)
    print("YES")     # 모두가 참일 때만 참이 됨.
else:
    print("NO")

if all(50 > x for x in a):     # 조건에서 하나라도 거짓이 되면 false return(boolean 형태로 답이 나옴.)
    print("YES")     # 모두가 참일 때만 참이 됨.
else:
    print("NO")

if any(15 > x for x in a):     # 조건에서 하나라도 참이 되면 true return(boolean 형태)
    print("YES")
else:     # 모두 거짓이어야 else로 넘어갈 수 있다.
    print("NO")

if any(11 > x for x in a):     # 조건에서 하나라도 참이 되면 true return(boolean 형태)
    print("YES")
else:     # 모두 거짓이어야 else로 넘어갈 수 있다.
    print("NO")
    
